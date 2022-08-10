class Order:
    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.items.append(quantity)
        self.items.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total = self.quantities[i] * self.prices[i]
            return total

    def pay(self, payment_type, security_code):
        if payment_type == "debit":
            print("processing debit payment type")
            print(f"verifying security code: {security_code}")
            self.status = "paid"
        elif payment_type == "credit":
            print("processing credit payment type")
            print(f"verifying security code: {security_code}")
            self.status = "paid"
        else:
            raise Exception(f"unknown payment type:{payment_type}")


order = Order()
order.add_item("chocolate", 2, 20)
order.total_price()
order.pay("debit", 3425345)