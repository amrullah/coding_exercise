# Coding Exercise: Invoice Total Calculator

Create a program that
1. Takes in a list of [InventoryItems](entities/inventory_item.py#L5)
2. Calculates the `subtotal` by adding `InventoryItem.selling_price`
3. Applies `discount` on the `subtotal`
4. Calculates and adds the `tax` amount on the `discount applied subtotal`, based on the [country](constants.py#L9)
   (do this if there's time)
5. And returns the above amount as `total invoice amount`

#### Discount Rules:
Discount is to be calculated on subtotal using the [Coupon](entities/coupon.py#L7) object, which will be supplied as an input.
There are two [Discount types](constants.py#L4), `Flat` and `Percentage`.
* `Flat` means that the mentioned `discount_value` is to be deducted from the subtotal
* `Percentage` means that the mentioned `discount_value` is the percentage of the subtotal to be deducted

`max_discount` is the maximum reduction that is permitted. Discount applied should not exceed this amount.

Also ensure that the `discount` amount should not exceed the `subtotal` itself. In other words, resultant subtotal after
applying the discount should not be negative.

#### Taxation Rules: (If there's time)
Taxation is to be calculated on the `subtotal after discount` has been applied. 
Taxation rules depend on the `country`, which will be supplied as an input.
* For Malaysia, if the `subtotal after discount` is >= 1000 the tax rate is 8%, else, the tax rate is 5%
* For Indonesia, the tax rate is flat 5%, regardless of the value of `subtotal after discount`

### How to proceed
In [main.py](main.py) you'll see a class `InvoiceTotalCalculator` containing the method `get_invoice_total()`. Start writing the solution from there.

To execute your code, you can run the test class in [tests.py](tests.py). It contains sample items and coupons to save you time.
In PyCharm, you can run the test class using the green play button, which will be visible near the line numbers.
In other Editors, you'll have to run from terminal using 
```
python3 -m unittest tests.InvoiceTaxCalculatorTestCase
```
----
Note: all the required entities like `InventoryItem`, `Coupon` and constants like `DiscountTypes` and `Countries` are already declared. You need not redeclare them.