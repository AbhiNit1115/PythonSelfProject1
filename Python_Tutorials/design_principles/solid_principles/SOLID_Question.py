from abc import ABC, abstractmethod


# A framework is integrated with allure report
# Concrete class Report having actual implementation of allure
from math import pi


class Report:

    def allure_report(self):
        print("this is allure report implementation")

# Ask is to add two new reporting mechanism to the existing framework let's say X-ray and Zephyr


    class GeometricalShape(ABC):
        @abstractmethod
        def calculate_area(self):
            pass

        @abstractmethod
        def calculate_radius(self):
            pass


    class Circle(GeometricalShape):
        def __init__(self, radius):
            self.radius = radius

        def calculate_area(self):
            pass

        def calculate_radius(self):
            return 2 * pi * self.radius


    class Square(GeometricalShape):
        def __init__(self, side):
            self.side = side

        def calculate_area(self):
            return self.side ** 2

        def calculate_radius(self):
            pass


    class Rectangle(GeometricalShape):
        def __init__(self, length, width):
            self.length = length
            self.width = width

        def calculate_area(self):
            return self.length * self.width

        def calculate_radius(self):
            pass
