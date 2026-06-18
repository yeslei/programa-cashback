from typing import Dict
import argparse
import json


def compute_cashback(
    price: float,
    discount_pct: float = 0.0,
    is_vip: bool = False
) -> Dict[str, float]:

    if price < 0:
        raise ValueError("O preço deve ser não negativo.")

    if not (0 <= discount_pct <= 100):
        raise ValueError("discount_pct deve estar entre 0 e 100.")

    # Valor da compra após desconto
    final_price = price * (1 - discount_pct / 100)

    # Cashback base (5%)
    base_cashback = 0.05 * final_price

    # Bônus VIP: 10% sobre o cashback base
    vip_bonus = 0.10 * base_cashback if is_vip else 0.0

    # Cashback total antes da promoção
    subtotal_cashback = base_cashback + vip_bonus

    # Promoção: dobra o cashback total para compras acima de R$ 500
    if final_price > 500:
        total_cashback = subtotal_cashback * 2
    else:
        total_cashback = subtotal_cashback

    return {
        "price": round(price, 2),
        "discount_pct": round(discount_pct, 2),
        "final_price": round(final_price, 2),
        "base_cashback": round(base_cashback, 2),
        "vip_bonus": round(vip_bonus, 2),
        "total_cashback": round(total_cashback, 2),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Calculadora de cashback"
    )

    parser.add_argument(
        "--price",
        type=float,
        default=600.0,
        help="Preço original do produto"
    )

    parser.add_argument(
        "--discount",
        type=float,
        default=20.0,
        help="Percentual de desconto (ex.: 20)"
    )

    parser.add_argument(
        "--vip",
        action="store_true",
        help="Indica que o cliente é VIP"
    )

    args = parser.parse_args()

    result = compute_cashback(
        price=args.price,
        discount_pct=args.discount,
        is_vip=args.vip
    )

    print(json.dumps(result, indent=2, ensure_ascii=False))

    print("\nExemplo de execução:")
    print("python cashback.py --price 600 --discount 20 --vip")
