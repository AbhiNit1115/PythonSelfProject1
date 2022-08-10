# A class should be Open for extension, meaning that the class’s behavior can be extended; and
# Closed for modification, meaning that the source code is set and cannot be changed.
# from our previous example suppose we want to introduce a new payment method apart from credit/debit say
# bitcoin payment

from abc import ABC, abstractmethod


class Request:
    products = []
    product_count = []
    product_prices = []
    status = "none"

    def add_product(self, name: str, quantity: int, price: int):
        self.products.append(name)
        self.products.append(quantity)
        self.products.append(price)

    def final_price(self):
        total = 0
        for i in range(len(self.product_prices)):
            total = self.product_count[i] * self.product_prices[i]
            return total


class PaymentProcessor(ABC):
    @abstractmethod
    def payment_method(self, req, security_code):
        pass


class DebitPayment(PaymentProcessor):
    def payment_method(self, req, security_code):
        print("processing debit payment type")
        print(f"verifying security code: {security_code}")
        req.status = "paid"


class CreditPayment(PaymentProcessor):
    def payment_method(self, req, security_code):
        print("processing credit payment type")
        print(f"verifying security code: {security_code}")
        req.status = "paid"


# Now in case we want to add another payment type say paypal, bitcoin etc. we don't have to violate O/C principle.

class ETHPayment(PaymentProcessor):
    def payment_method(self, req, security_code):
        print("processing btc payment type")
        print(f"verifying security code: {security_code}")
        req.status = "paid"


req = Request()
req.add_product("chocolate", 2, 20)
req.add_product("ssd", 2, 20)
print(req.final_price())

payment = ETHPayment()
payment.payment_method(req, 3425345)
