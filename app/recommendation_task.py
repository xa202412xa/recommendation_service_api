from app import models, database
from sqlalchemy.future import select

async def recommendation_task(user_id: str):
    async with database.SessionLocal() as session:
        # Получите историю покупок пользователя
        result = await session.execute(select(models.Purchase).where(models.Purchase.user_id == user_id))
        purchases = result.scalars().all()
        
        # Логика для анализа покупок и генерации рекомендаций
        recommendations = []
        for purchase in purchases:
            # Пример: рекомендуем товары из той же категории
            result = await session.execute(select(models.Item).where(models.Item.category == purchase.item.category))
            similar_items = result.scalars().all()
            recommendations.extend(similar_items)
        
        # Удалите дубликаты и верните рекомендации
        unique_recommendations = list(set(recommendations))
        return unique_recommendations
