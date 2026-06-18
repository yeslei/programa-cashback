from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
from . import schemas, crud, db as _db, services

router = APIRouter()


@router.post('/calculate', response_model=schemas.CalculateResponse)
def calculate_cashback(payload: schemas.CalculateRequest, request: Request, db: Session = Depends(_db.get_db)):
    # Valida input
    client_type = payload.client_type.lower()
    if client_type not in ('normal', 'vip'):
        raise HTTPException(status_code=400, detail='client_type deve ser "normal" ou "vip"')

    price = payload.price
    discount = payload.discount_pct or 0.0
    is_vip = (client_type == 'vip')

    # Calcula cashback
    result = services.compute_cashback(price=price, discount_pct=discount, is_vip=is_vip)

    # Pega IP do cliente
    client_ip = request.client.host

    # Persiste consulta
    crud.create_query(db=db, ip=client_ip, client_type=client_type, price=price, discount_pct=discount, is_vip=is_vip, cashback=result['total_cashback'])

    return schemas.CalculateResponse(
        price=result['price'],
        discount_pct=result['discount_pct'],
        final_price=result['final_price'],
        base_cashback=result['base_cashback'],
        vip_bonus=result['vip_bonus'],
        total_cashback=result['total_cashback'],
    )


@router.get('/history', response_model=list[schemas.QueryOut])
def history(request: Request, db: Session = Depends(_db.get_db)):
    client_ip = request.client.host
    records = crud.get_history_by_ip(db=db, ip=client_ip)
    return records
