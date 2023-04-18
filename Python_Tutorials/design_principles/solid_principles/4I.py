# The general idea of interface segregation principle is that it’s better to have a lot of smaller interfaces
# than a few bigger ones i.e. make fine grained interfaces that are client-specific. Clients should not be
# forced to implement interfaces they do not use.
# For software engineers, this means that you don’t want to just start with an existing interface and add new
# methods. Instead, start by building a new interface and then let your class implement multiple interfaces as
# needed. Smaller interfaces mean that developers should have a preference for composition over inheritance and
# for decoupling over coupling. According to this principle, engineers should work to have many client-specific
# interfaces, avoiding the temptation of having one big, general-purpose interface.

# Now continuing with our prior example from LSP, here suppose the rupay payment has email approval and the
# upi payment has duo approval so if we depend on the large interface i.e. AcceptedPaymentTypes and create
# a new method in rupay and another in upi payment then we are breaking the LSP. So, in order to achieve it we
# would use interface segregation i.e. create another interface for approval process.

# Dependency inversion means that we want our class to depend on abstractions and not on concrete subclasses
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


class AcceptedPaymentTypes(ABC):
    """Interface for different payment types"""

    @abstractmethod
    def payment_type(self):
        pass


class DuoApproval:
    """Class for Duo Approval implementing Approval Interface for duo mobile type approval"""
    approved = False

    def duo_code_auth(self, duo_code):
        print(f"Verifying duo code: {duo_code}")
        self.approved = True

    def approval_status(self) -> bool:
        return self.approved


class EmailApproval:
    """Class for Email Approval implementing Approval Interface for email type approval"""
    approved = False

    def email_code_auth(self, email_code: str):
        print(f"Verifying email code: {email_code}")
        self.approved = True

    def approval_status(self) -> bool:
        return self.approved


class RupayPayment(AcceptedPaymentTypes):
    """Now applying ISP RupayPayment has email approval so created approval parameter of
       EmailApproval type"""

    def __init__(self, cvv_pin: int, approval: EmailApproval):
        self.cvv_pin = cvv_pin
        self.approval = approval

    def payment_type(self):
        if not self.approval.approval_status():
            print("Not Approved")
        else:
            print("Approved")
        print("processing rupay payment type")
        print(f"verifying security code: {self.cvv_pin}")


class UPIPayment(AcceptedPaymentTypes):
    """Now applying ISP UPIPayment has duo approval so created approval parameter of
       duoApproval type"""

    def __init__(self, upi_code: int, approval: DuoApproval):
        self.upi_code = upi_code
        self.approval = approval

    def payment_type(self):
        if not self.approval.approval_status():
            print("Not Approved")
        else:
            print("Approved")
        print("processing rupay payment type")
        print(f"verifying security code: {self.upi_code}")


tur = Tournament()
tur.create_games("Bowling", 1, 23)
tur.games_count(1)

approval_type1 = EmailApproval()
payment = RupayPayment(435, approval_type1)
approval_type1.email_code_auth("4234")
payment.payment_type()
print("___________________________________")

approval_type2 = DuoApproval()
approval_type2.duo_code_auth(6456)
payment.payment_type()

# Accepted Payment Types are dependent on concrete class which is email and duo auth we want to depend on
# abstraction
