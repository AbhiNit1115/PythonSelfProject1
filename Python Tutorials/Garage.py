class FreeGarageNotFound(Exception):
    pass


class Car:

    CLASSIC_CAR_ABBREVIATION = "C"
    SIMPLE_CAR_ABBREVIATION = "S"

    def __init__(self, manufacturer, model, year, is_classic):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.is_classic = is_classic

    def __repr__(self):
        is_classic = (
            Car.CLASSIC_CAR_ABBREVIATION
            if self.is_classic
            else Car.SIMPLE_CAR_ABBREVIATION
        )
        return (
            f"Manufacturer - {self.manufacturer}, "
            f"model - {self.model}, year - {self.year}, "
            f"is_classic - {is_classic}"
        )


class GarageService:
    SECURE_GARAGES = [1, 7]
    SIMPLE_GARAGES = [2, 3, 4, 5, 6]

    def __init__(self, garage_cleaning_service) -> None:
        self.garage_cleaning_service = garage_cleaning_service
        self.garages_with_car = dict()

    def register_in_garage(self, car):
        garages = (
            GarageService.SECURE_GARAGES
            if car.is_classic
            else GarageService.SIMPLE_GARAGES
        )
        garage = self.find_free_garage_from(garages)

        if not garage:
            raise FreeGarageNotFound

        self.clean(garage)
        self.register_car(garage, car)

        return garage

    def clean(self, garage):
        self.garage_cleaning_service.clean(garage)

    def register_car(self, garage, car):
        self.garages_with_car[garage] = car

    def is_garage_free(self, garage):
        return garage in self.garages_with_car

    def find_free_garage_from(self, garages):
        for garage in garages:
            result = self.is_garage_free(garage)
            if not result:
                return garage
        return None

