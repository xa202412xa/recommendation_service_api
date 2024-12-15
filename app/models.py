from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base
from uuid import uuid4
from datetime import datetime

class UserPurchases(Base):
    __tablename__ = "UserPurchases"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True), index=True)
    item_id = Column(UUID(as_uuid=True))
    category = Column(String)
    purchase_date = Column(DateTime, default=datetime.utcnow)

class Items(Base):
    __tablename__ = "Items"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String)
    category = Column(String)

class Recommendations(Base):
    __tablename__ = "Recommendations"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True), index=True)
    item_id = Column(UUID(as_uuid=True))
