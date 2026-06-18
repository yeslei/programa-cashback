from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CalculateRequest(BaseModel):
    client_type: str
    price: float
    discount_pct: Optional[float] = 0.0


class CalculateResponse(BaseModel):
    price: float
    discount_pct: float
    final_price: float
    base_cashback: float
    vip_bonus: float
    total_cashback: float


class QueryOut(BaseModel):
    id: int
    ip: str
    client_type: str
    price: float
    discount_pct: float
    is_vip: bool
    cashback: float
    created_at: datetime

    class Config:
        orm_mode = True
