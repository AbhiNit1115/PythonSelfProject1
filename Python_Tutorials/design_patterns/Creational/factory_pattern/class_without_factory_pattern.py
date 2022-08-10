import abc


class Television(metaclass=abc.ABCMeta):
    """Created an Interface and extended it to suit different Television functionality"""

    @abc.abstractmethod
    def smart_tv(self):
        pass

    @abc.abstractmethod
    def ultra_hd(self):
        pass


class Samsung(Television):
    """Concrete class Samsung that will implement the TV functionality"""

    def __init__(self, os, oled):
        self.os = os
        self.oled = oled

    def smart_tv(self):
        return self.os

    def ultra_hd(self):
        return self.oled


class Sony(Television):
    """Concrete class Sony that will implement the TV functionality"""

    def __init__(self, os, qled):
        self.os = os
        self.qled = qled

    def smart_tv(self):
        return self.os

    def ultra_hd(self):
        return self.qled


sam = Samsung("iOS", "OLED")
print("The TV OS is:", sam.smart_tv())
son = Sony("Android", "QLED")
print("The TV screen type is:", son.ultra_hd())
