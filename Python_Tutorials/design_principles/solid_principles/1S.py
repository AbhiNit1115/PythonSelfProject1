# S: single Responsibility Principle: A class and its respective methods should only have one responsibility.
# In the below mentioned example we have one class which is doing things like game creation, counting
# total games as well as defining the game payment method which is not in line with SRP.

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


class GamePaymentMethods:
    """ we have remove payment method instead of that we have created this class game payment method
        here we no longer need the paying_methods as we are explicitly defining the payment method"""

    @staticmethod
    def cash_payment():
        print("Cash Payment no security code required")
        status = "Registered"
        print("Status is:", status)

    @staticmethod
    def rupay_payment(cvv_pin):
        print("Rupay payment mode selected")
        print(f"the cvv pin is: {cvv_pin}")
        status = "Registered"
        print("Status is:", status)


tur = Tournament()
tur.create_games("Bowling", 1, 23)
tur.games_count(1)
game_pay = GamePaymentMethods
game_pay.rupay_payment(4554)
game_pay.cash_payment()
