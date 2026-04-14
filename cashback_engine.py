"""
Cashback System v1.0
Logic to calculate base cashback and VIP bonuses.
Author: Lucas Faria
Date: April 2026
"""

BASE_CASHBACK_RATE = 0.05       # 5% base rate
VIP_BONUS_RATE = 0.10           # 10% extra for VIPs
PROMOTION_THRESHOLD = 500.0     # Value required to trigger multiplier
PROMOTION_MULTIPLIER = 2        # Multiplies the rate if threshold is met

def calculate_cashback(purchase_value: float, is_vip: bool) -> float:
    """
    Calculates the final cashback amount based on the purchase amount and VIP status.
    """
    # Defines the applicable rates
    current_rate = BASE_CASHBACK_RATE
    if purchase_value > PROMOTION_THRESHOLD:
        current_rate *= PROMOTION_MULTIPLIER

    # Calculate base cashback and apply VIP bonus
    cashback = purchase_value * current_rate

    # Apply VIP bonus over the base result
    if is_vip:
        cashback += (cashback * VIP_BONUS_RATE)

    return cashback

def calculate_net_price(gross_value: float, discount_percentage: float) -> float:
    """
    Calculates the final price after applying a discount.
    """
    discount_amount = gross_value * (discount_percentage / 100)
    return gross_value - discount_amount

if __name__ == "__main__":
    # Example
    gross = 600.0
    discount = 15.0
    is_customer_vip = False

    final_price = calculate_net_price(gross, discount)
    final_cashback = calculate_cashback(final_price, is_customer_vip)

    print(f"Purchase Value: R$ {final_price:.2f}")
    print(f"Cashback: R$ {final_cashback:.2f}")