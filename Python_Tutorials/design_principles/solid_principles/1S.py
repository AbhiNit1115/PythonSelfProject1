# S: single Responsibility Principle: A class and its respective methods should only have one responsibility.
# In the below mentioned example we have one class which is doing things like addition of orders, calculation
# of total price as well as defining the payment method type which is not in line with SRP.

class Request:
    products = []
    product_count = []
    product_prices = []

    def add_product(self, name: str, quantity: int, price: int):
        self.products.append(name)
        self.products.append(quantity)
        self.products.append(price)

    def final_price(self):
        total = 0
        for i in range(len(self.product_prices)):
            total = self.product_count[i] * self.product_prices[i]
            return total

    def payment_mode_debit(self, cvv_pin):
        print("Payment mode selected is debit")
        print(f"the cvv pin is: {cvv_pin}")

    def payment_mode_credit(self, cvv_pin):
        print("Payment mode selected is credit")
        print(f"the cvv pin is: {cvv_pin}")


req = Request()
req.add_product("cream", 5, 6)
req.add_product("cream1", 5, 6)
print(req.final_price())
req.payment_mode_debit(876876)
req.payment_mode_credit(52432)


# here we can remove the payment method instead of that we have created below mentioned class payment processor
# also as there is no "status" variable defined at class level we have passed a parameter "order" and verifying
# the status with order.status


class PaymentProcessor:

    def payment_mode_debit(self, cvv_pin):
        print("Payment mode selected is debit")
        print(f"the cvv pin is: {cvv_pin}")

    def payment_mode_credit(self, cvv_pin):
        print("Payment mode selected is credit")
        print(f"the cvv pin is: {cvv_pin}")


payment = PaymentProcessor
payment.payment_mode_debit(456, 6757)
