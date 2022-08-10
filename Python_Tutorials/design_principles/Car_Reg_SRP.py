# S: single Responsibility Principle: A class and its respective methods should only have one responsibility.
# In the below mentioned example we have one class which is doing things like having car details, checking
# registration status and sending notifications which is not in line with SRP.

class CarRegistration:

    def __init__(self, model, number_plate, status):
        self.model = model
        self.number_plate = number_plate
        self.status = status

    def registration_status(self):
        if self.status:
            print("car is registered")
        else:
            print("car is not registered")

    def car_details(self):
        print("model is:", self.model)
        print("number is", self.number_plate)

    def notification(self):
        if self.status == "Registered":
            print("send notification")
        else:
            print("car not registered so no notification")


reg = CarRegistration("Toyota Prius", "KA06KK8999", "Registered")
reg.registration_status()
reg.car_details()
reg.notification()
print("____________________________")


class CarReg:

    def __init__(self, status):
        self.status = status

    def registration_status(self):
        if self.status:
            print("car is registered")
        else:
            print("car is not registered")

    def notification(self):
        if self.status == "Registered":
            print("send notification")
        else:
            print("car not registered so no notification")


reg2 = CarReg("Unregistered")
reg2.registration_status()
reg2.notification()
print("____________________________")


class CarDetails:

    def __init__(self, model, number_plate):
        self.model = model
        self.number_plate = number_plate

    def car_details(self):
        print("model is:", self.model)
        print("number is", self.number_plate)


details = CarDetails("Toyota Prius", "KA07JJ3456")
details.car_details()
