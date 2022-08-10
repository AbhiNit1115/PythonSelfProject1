# The general idea of interface segregation principle is that it’s better to have a lot of smaller interfaces
# than a few bigger ones i.e. make fine grained interfaces that are client-specific. Clients should not be
# forced to implement interfaces they do not use.
# For software engineers, this means that you don’t want to just start with an existing interface and add new
# methods. Instead, start by building a new interface and then let your class implement multiple interfaces as
# needed. Smaller interfaces mean that developers should have a preference for composition over inheritance and
# for decoupling over coupling. According to this principle, engineers should work to have many client-specific
# interfaces, avoiding the temptation of having one big, general-purpose interface.

# Now continuing with our prior example from LSP, here suppose the debit card has 2F authentication and the
# credit card doesn't have it so if we depend on the large interface i.e. PaymentProcessor and create
# a new method in debit payment processor then we are breaking the LSP. So, in order to achieve it we would use
# interface segregation i.e. create another interface for 2f auth.

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


# Interface1: for payment method.
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass


# Interface2: This is another granular interface which is a child of interface1 i.e. PaymentProcessor for 2F
class PaymentProcessor_2F(PaymentProcessor):
    @abstractmethod
    def sms_auth(self, two_fact):
        pass


# Now applying interface segregation principle we can create a class for debit payment and in that if we want
# we can implement either one or both the methods.
class Debit_payment_processor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("processing debit payment type")
        print(f"verifying security code: {self.security_code}")
        order.status = "paid"

    def sms_auth(self, two_fact):
        print(f"This is two factor auth: {two_fact}")


# The credit method doesn't uses 2F auth hence no need of implementing the method here (ISP advantage)
class Credit_payment_processor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("processing credit payment type")
        print(f"verifying security code: {self.security_code}")
        order.status = "paid"


# Now BTC class uses 2F authentication then it needs to implement the method
class Btc_payment_processor(PaymentProcessor):
    def __init__(self, hash_code):
        self.hash_code = hash_code

    def pay(self, order):
        print("processing btc payment type")
        print(f"verifying security code: {self.hash_code}")
        order.status = "paid"

    def sms_auth(self, two_fact):
        print(f"This is two factor auth: {two_fact}")


order = Order()
order.add_item("chocolate", 2, 20)
order.add_item("ssd", 2, 20)
order.total_price()

# Now we can create objects for diff classes like debit, credit etc.
payment1 = Debit_payment_processor("34656546e")  # user has to pass the parameter here for security_code
payment1.pay(order)
payment1.sms_auth("345re")
print("_______________________________________")

payment2 = Btc_payment_processor("This is Hash Code")  # user has to pass the parameter here for hash_code
payment2.pay(order)
payment2.sms_auth("65765")
