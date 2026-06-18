from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
from . import schemas, crud, db as _db, services

router = APIRouter()


def get_client_ip(request: Request) -> str:
    forwarded_for = request.headers.get('x-forwarded-for')
    if forwarded_for:
        return forwarded_for.split(',')[0].strip()

    real_ip = request.headers.get('x-real-ip')
    if real_ip:
        return real_ip.strip()

    return request.client.host


@router.post('/calculate', response_model=schemas.CalculateResponse)
def calculate_cashback(payload: schemas.CalculateRequest, request: Request, db: Session = Depends(_db.get_db)):
    # Valida input
    client_type = payload.client_type.lower()
    if client_type not in ('normal', 'vip'):
        raise HTTPException(status_code=400, detail='client_type deve ser "normal" ou "vip"')

    price = payload.price
    discount = payload.discount_pct or 0.0

    # Calcula cashback
    result = services.compute_cashback(price=price, discount_pct=discount, client_type=client_type)

    # Pega IP do cliente
    client_ip = get_client_ip(request)

    # Persiste consulta
    crud.create_query(db=db, ip=client_ip, client_type=client_type, price=price, discount_pct=discount, cashback=result['total_cashback'])

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
    client_ip = get_client_ip(request)
    records = crud.get_history_by_ip(db=db, ip=client_ip)
    return records
