from dataclasses import dataclass

from constants import DiscountTypes


@dataclass(frozen=True)
class Coupon:
    name: str
    discount_type: DiscountTypes
    discount_value: float
    max_discount: float
