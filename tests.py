import logging
import unittest

from constants import DiscountTypes, Countries
from entities import InventoryItem, Coupon
from main import InvoiceTotalCalculator


class InvoiceTaxCalculatorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.inventory_items = [InventoryItem(name="Item1", selling_price=100),
                                InventoryItem(name="Item2", selling_price=150),
                                InventoryItem(name="Item3", selling_price=250)]

        self.flat_coupon = Coupon(name="Flat200", discount_type=DiscountTypes.FLAT,
                                  discount_value=200.0, max_discount=200.0)

        self.percentage_coupon = Coupon(name="Party10", discount_type=DiscountTypes.PERCENTAGE,
                                        discount_value=10.0, max_discount=40.0)

        self.invoice_total_calculator = InvoiceTotalCalculator()

    def test_nothing_flat_discount(self):
        invoice_total = self.invoice_total_calculator.calculate_invoice_total(self.inventory_items, self.flat_coupon,
                                                                              Countries.INDONESIA)
        print(f"invoice total is: {invoice_total}\n")

    def test_nothing_percentage_discount(self):
        invoice_total = self.invoice_total_calculator.calculate_invoice_total(self.inventory_items,
                                                                              self.percentage_coupon,
                                                                              Countries.INDONESIA)
        print(f"invoice total is: {invoice_total}\n")