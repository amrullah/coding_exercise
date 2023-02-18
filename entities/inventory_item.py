from dataclasses import dataclass


@dataclass(frozen=True)
class InventoryItem:
    name: str
    selling_price: float
