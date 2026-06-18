from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from .db import Base
from datetime import datetime


class Query(Base):
    __tablename__ = 'queries'

    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String(100), index=True, nullable=False)
    client_type = Column(String(20), nullable=False)
    price = Column(Float, nullable=False)
    discount_pct = Column(Float, nullable=False)
    is_vip = Column(Boolean, nullable=False, default=False)
    cashback = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
