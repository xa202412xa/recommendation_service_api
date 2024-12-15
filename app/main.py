from fastapi import FastAPI
from app import models, schemas, database, recommendation_task
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.future import select
from uuid import uuid4
from datetime import datetime
import asyncio

DATABASE_URL = "postgresql+asyncpg://user:password@localhost/dbname"

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
Base = declarative_base()

app = FastAPI()

@app.post("/purchases")
async def add_purchases(request: schemas.PurchaseRequest):
    async with SessionLocal() as session:
        async with session.begin():
            for item in request.cart:
                purchase = models.UserPurchases(
                    user_id=request.user_id,
                    item_id=item.item_id,
                    category=item.category
                )
                session.add(purchase)
        await session.commit()
    return {"status": "purchases_added"}

@app.post("/generate_recommendations")
async def generate_recommendations(user_id: str):
    asyncio.create_task(recommendation_task.recommendation_task(user_id))
    return {"status": "recommendations_generation_started"}

@app.get("/recommendations")
async def get_recommendations(user_id: str):
    async with SessionLocal() as session:
        result = await session.execute(select(models.Recommendations).where(models.Recommendations.user_id == user_id))
        recommendations = result.scalars().all()
        return {"recommendations": recommendations}
