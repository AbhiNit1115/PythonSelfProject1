# A class should be Open for extension, meaning that the class’s behavior can be extended; and
# Closed for modification, meaning that the source code is set and cannot be changed.
# from our previous example suppose we want to introduce a new payment method apart from cash/rupay say
# UPI payment

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
    """Created an interface for all accepted payment types"""
    @abstractmethod
    def payment_type(self, cvv_pin):
        pass


class RupayPayment(AcceptedPaymentTypes):

    """Implementing the interface method as per the need of class"""
    def payment_type(self, cvv_pin):
        print("Rupay payment mode selected")
        print(f"the cvv pin is: {cvv_pin}")
        status = "Registered"
        print("Status is:", status)


class CashPayment(AcceptedPaymentTypes):
    """Implementing the interface method as per the need of class"""
    def payment_type(self, cvv_pin):
        print("Cash Payment no security code required")
        status = "Registered"
        print("Status is:", status)


class UPIPayment(AcceptedPaymentTypes):

    """If we want to add another payment type say UPI etc. we don't have to violate O/C principle."""
    def payment_type(self, cvv_pin):
        print("UPI payment mode selected")
        print(f"the upi pin is: {cvv_pin}")
        status = "Registered"
        print("Status is:", status)


tur = Tournament()
tur.create_games("Bowling", 1, 23)
tur.games_count(1)
payment = UPIPayment()
payment.payment_type(3425345)
