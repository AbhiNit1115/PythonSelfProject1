# Liskov Substitution Principle: Broadly, this principle simply requires that every derived class should
# be substitutable for its parent class. What is wanted here is something like the following substitution property:
# if for each object O1 of type S there is an object O2 of type T such that for all programs P defined in terms of
# T, the behavior of P is unchanged when O1 is substituted for O2 then S is a subtype of T.

# From the previous example of the open closed principle we have created an interface class for payment and from
# that interface we are deriving child classes. Now our child class UPI doesn't use cvv pin but it uses
# upi code so if we are passing upi codes as security codes then we are violating open close principle as well
# as LSP so here is a way to do it.


from abc import ABC, abstractmethod


class Tournament:
    events = []
    teams = []
    pricing = []
    status = "open"

    def create_games(self, games: str, count: int, price: int):
        self.events.append(games)
        self.teams.append(count)
        self.pricing.append(price)

    def games_count(self, total_games: int):
        self.events.append(total_games)
        total_events = len(self.events)
        print("Total Games in Tournament:", total_events)


# Now in order to implement LSP we have to first remove the security code from the parent class and the create
# a constructor and pass security_code/upi_pin as a parameter to all the subclasses which will be using them.
class AcceptedPaymentTypes(ABC):
    @abstractmethod
    def payment_type(self):
        pass


class RupayPayment(AcceptedPaymentTypes):

    """Now applying LSP for parent class AcceptedPaymentTypes the respective child class RupayPayment
     should be complete substitute."""
    def __init__(self, cvv_pin: int):
        self.cvv_pin = cvv_pin

    def payment_type(self):
        print("Rupay payment mode selected")
        print(f"the cvv pin is: {self.cvv_pin}")
        status = "Registered"
        print("Status is:", status)


class CashPayment(AcceptedPaymentTypes):

    def payment_type(self):
        print("Cash Payment no security code required")
        status = "Registered"
        print("Status is:", status)


class UPIPayment(AcceptedPaymentTypes):

    """Now even if the class UPI method is using upi code instead of cvv code it is in complete alignment with
       LSP i.e. it is completely substitutable for parent class"""

    def __init__(self, upi_code: int):
        self.upi_code = upi_code

    def payment_type(self):
        print("UPI payment mode selected")
        print(f"the upi code is: {self.upi_code}")
        status = "Registered"
        print("Status is:", status)


tur = Tournament()
tur.create_games("Bowling", 1, 23)
tur.games_count(1)
payment1 = UPIPayment(3425345)
payment1.payment_type()
print("_______________________")
payment2 = RupayPayment(2342)
payment2.payment_type()
print("_______________________")
payment3 = CashPayment
payment3.payment_type(CashPayment)
