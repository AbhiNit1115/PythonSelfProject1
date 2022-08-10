# Liskov Substitution Principle: Broadly, this principle simply requires that every derived class should
# be substitutable for its parent class. What is wanted here is something like the following substitution property:
# if for each object O1 of type S there is an object O2 of type T such that for all programs P defined in terms of
# T, the behavior of P is unchanged when O1 is substituted for O2 then S is a subtype of T.

# From the previous example of the open closed principle we have created an interface class for payment and from
# that interface we are deriving child classes. Now our child class BTC doesn't use security code but it uses
# hash codes so if we are passing hash codes as security codes then we are violating open close principle as well
# as LSP so here is a way to do it.


from abc import ABC, abstractmethod


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
            total += self.quantities[i] * self.prices[i]
            return total


# Now in order to implement LSP we have to first remove the security code from the parent class and the create
# a constructor and pass security_code/hash_code as a parameter to all the subclasses which will be using them.
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass


# Now applying LSP the parent class has only one variable and the respective child classes should also
# be complete substitute of the parent class (in our case having only one parameter).
class Debit_payment_processor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("processing debit payment type")
        print(f"verifying security code: {self.security_code}")
        order.status = "paid"


class Credit_payment_processor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("processing credit payment type")
        print(f"verifying security code: {self.security_code}")
        order.status = "paid"


# Now even if the class BTC method is using hash code instead of security code it is in complete alignment with
# LSP i.e. it is completely substitutable for parent class

class Btc_payment_processor(PaymentProcessor):
    def __init__(self, hash_code):
        self.hash_code = hash_code

    def pay(self, order):
        print("processing btc payment type")
        print(f"verifying security code: {self.hash_code}")
        order.status = "paid"


order = Order()
order.add_item("chocolate", 2, 20)
order.add_item("ssd", 2, 20)
print(order.total_price())

payment = Btc_payment_processor("This is Hash Code")  # now user has to pass the parameter here
payment.pay(order)
