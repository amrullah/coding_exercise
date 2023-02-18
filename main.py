from constants import Countries, DiscountTypes
from entities import Coupon, InventoryItem


class InvoiceTotalCalculator:
    def calculate_invoice_total(self, items: list[InventoryItem], coupon: Coupon, country: Countries) -> float:
        # TODO: do something here
        # Refresher:
        # objects exist to represent a concept in the domain
        # recall 4 principles:
        # 1. Abstraction: giving a higher meaning to the primitive building blocks
        # 2. Decomposition: Break down a component into smaller subordinate components, for better focus (or cohesion)
        # 3. Encapsulation: Suppressing the internal details and exposing a simplified interface
        # 4. Variation management: If a concept has variations, capture the common in superclass and the variant in
        #    subclass
        return 0.0
