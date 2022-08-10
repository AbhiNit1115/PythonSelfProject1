class AutoRacing:

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


car1 = AutoRacing(brand="toyota", speed=120, agility="3.5")
car2 = AutoRacing(brand="honda", speed=110, agility="4.5")
car3 = AutoRacing(brand="suzuki", speed=115, agility="5.5")

car1.race(car2)
car1.surpass(car3)
