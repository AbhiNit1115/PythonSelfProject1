# Decorator can be recognized by creation methods or constructor that accept objects of the same class
# or interface as a current class.

class Gun:
    def __init__(self, recoil, fire_speed):
        self.recoil = recoil
        self.fire_speed = fire_speed

    def bullets_fired(self):
        print("gun aim and fire")
        return self.recoil + self.fire_speed


class UZIMachineGun:
    def __init__(self, recoil, fire_speed):
        self.recoil = recoil
        self.fire_speed = fire_speed

    def bullets_fired(self):
        print("bullet fired for uzi machine gun")
        return self.recoil.bullets_fired() * self.fire_speed

    def gun_type(self, type1):
        print("LMG is an:", type1)


class LMG:
    def __init__(self, recoil, fire_speed):
        self.recoil = recoil
        self.fire_speed = fire_speed

    def bullets_fired(self):
        print("bullet fired for three knot three")
        return self.recoil.bullets_fired() ** self.fire_speed

    def gun_type(self, type2):
        print("LMG is an:", type2)


base_gun = Gun(2, 2)
uzi_base_gun = UZIMachineGun(base_gun, 5)
lmg_uzi_base_gun = LMG(uzi_base_gun, 10)
lmg_uzi_base_gun.gun_type("automatic")
total_bullets_fired = lmg_uzi_base_gun.bullets_fired()
print(total_bullets_fired)


