class Tournament:
    events = []
    teams = []
    pricing = []

    def create_games(self, games: str, count: int, price: int):
        self.events.append(games)
        self.teams.append(count)
        self.pricing.append(price)

    def games_count(self, total_games: int):
        self.events.append(total_games)
        total_events = len(self.events)
        print("Total Games in Tournament:", total_events)

    def game_payment(self, paying_methods: str, cvv_pin: int):
        if paying_methods == "cash":
            print("processing cash payment")
            status = "Registered"
            print("Status is:", status)
        elif paying_methods == "rupay":
            print("processing rupay payment")
            print(f"verifying security code: {cvv_pin}")
            status = "Registered"
            print("Status is:", status)
        else:
            raise Exception(f"unknown payment type:{paying_methods}")


tur = Tournament()
tur.create_games("Bowling", 1, 23)
tur.games_count(1)
tur.game_payment("rupay", 3425345)
tur.game_payment("cash", 435)
