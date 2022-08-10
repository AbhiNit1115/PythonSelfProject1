from abc import abstractmethod, ABC


class AutoRacingStrategy(ABC):

    @abstractmethod
    def surpass(self, competitor):
        pass

    @abstractmethod
    def race(self, top_speed):
        pass

    @abstractmethod
    def flexible(self, fitness):
        pass


class Car(AutoRacingStrategy):

    def __init__(self, brand=None, speed=None, agility=None):
        self.brand = brand
        self.speed = speed
        self.agility = agility

    def surpass(self, competitor):
        print("{0.brand} car overtook {1.brand}".format(self, competitor))

    def race(self, top_speed):
        print("{0.speed} top speed of car1 and {1.speed} top speed of car2".format(self, top_speed))

    def flexible(self, fitness):
        print("{0.agility} car overtook {1.agility}".format(self, fitness))


class GrandPrixContext:
    auto_racing_strategy: AutoRacingStrategy  # the strategy interface

    @staticmethod
    def race_car1_vs_car2():
        car1 = Car(speed=120)
        car2 = Car(speed=110)
        car1.race(car2)
        if car1.speed > car2.speed:
            print("car1 is winner")
        else:
            print("car2 is winner")

    @staticmethod
    def race_car1_vs_car3():
        car1 = Car(brand="Toyota")
        car3 = Car(brand="Mercedes")
        car1.surpass(car3)


mud_race = GrandPrixContext
mud_race.race_car1_vs_car2()
mud_race.race_car1_vs_car3()
