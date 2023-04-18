# Factory pattern is a creation pattern that defines an interface for creating an object and
# defers instantiation until runtime. This is used when we don't know how many or what type of objects will
# be needed until runtime.

# The Factory design pattern will help us abstract the available Television from the client, i.e. the client
# does not have to know all the Television available, but rather only create what they need during runtime. It
# will also allow us to centralize and encapsulate the object creation.

import abc


class ITelevision(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def smart_tv(self):
        pass

    @abc.abstractmethod
    def ultra_hd(self):
        pass


class LG(ITelevision):
    def __init__(self):
        self.os = "Android"
        self.oled = "oled"

    def smart_tv(self):
        return self.os

    def ultra_hd(self):
        return self.oled


class Onida(ITelevision):
    def __init__(self):
        self.os = "iOS"
        self.qled = "qled"

    def smart_tv(self):
        return self.os

    def ultra_hd(self):
        return self.qled


class TelevisionFactory:

    """TelevisionFactory class to select the specific Television classes based on the client's input"""

    @staticmethod
    def select_tv(tv_type):
        try:
            if tv_type == "Onida":
                return Onida()
        except:
            raise AssertionError("QLED Tv not available")
        try:
            if tv_type == "LG":
                return LG()
        except:
            raise AssertionError("Smart Tv not available")


tv = TelevisionFactory()
print(tv.select_tv("Onida").ultra_hd())
print(tv.select_tv("LG").smart_tv())