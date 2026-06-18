from typing import Dict


def compute_cashback(price: float, discount_pct: float = 0.0, is_vip: bool = False) -> Dict[str, float]:
    if price < 0:
        raise ValueError("O preço deve ser não negativo.")
    if not (0 <= discount_pct <= 100):
        raise ValueError("discount_pct deve estar entre 0 e 100.")

    final_price = price * (1 - discount_pct / 100)
    base_cashback = 0.05 * final_price
    vip_bonus = 0.10 * base_cashback if is_vip else 0.0
    subtotal = base_cashback + vip_bonus
    if final_price > 500:
        total = subtotal * 2
    else:
        total = subtotal

    return {
        "price": round(price, 2),
        "discount_pct": round(discount_pct, 2),
        "final_price": round(final_price, 2),
        "base_cashback": round(base_cashback, 2),
        "vip_bonus": round(vip_bonus, 2),
        "total_cashback": round(total, 2),
    }
