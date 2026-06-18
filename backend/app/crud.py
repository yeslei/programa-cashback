from . import models
from sqlalchemy.orm import Session
from datetime import datetime


def create_query(db: Session, *, ip: str, client_type: str, price: float, discount_pct: float, is_vip: bool, cashback: float):
    q = models.Query(
        ip=ip,
        client_type=client_type,
        price=price,
        discount_pct=discount_pct,
        is_vip=is_vip,
        cashback=cashback,
        created_at=datetime.utcnow()
    )
    db.add(q)
    db.commit()
    db.refresh(q)
    return q


def get_history_by_ip(db: Session, ip: str):
    return db.query(models.Query).filter(models.Query.ip == ip).order_by(models.Query.created_at.desc()).all()
