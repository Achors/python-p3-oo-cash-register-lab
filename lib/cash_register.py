#!/usr/bin/env python3

class CashRegister:
    # cash_register.py
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        for _ in range(quantity):
            self.items.append({"title": title, "price": price, "quantity": quantity})
            self.total += price
            self.last_transaction_amount = price

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def get_items(self):
        return [item["title"] for item in self.items]

    def void_last_transaction(self):
        if self.items:
            last_item = self.items.pop()
            self.total -= last_item["price"] * last_item["quantity"]
        else:
            self.total = 0


    # def apply_discount(self):
    #     if self.discount > 0:
    #         discount_amount = (self.discount / 100) * self.total
    #         self.total -= discount_amount
    #         return f"Discount applied: ${discount_amount} off. New total: ${self.total}"
    #     else:
    #         return "No discount applied."

    # def get_items(self):
    #     return self.items

    # def reset_total(self):
    #     self.total = 0
    #     self.items = []

    # def get_total(self):
    #     return self.total

