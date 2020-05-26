# name = "marine"
# hp = 40
# damage = 5
# print("{0} unit is maden".format(name))
# print("HP {0}, damage {1}".format(hp, damage))
#
#
# tank_name = "tank"
# tank_hp = 150
# tank_damage=35
# print("{0} unit is maden".format(tank_name))
# print("HP {0}, damage {1}".format(tank_hp, tank_damage))
#
# def attack(name, location, damage):
#     print("{0} : {1} attack damage{2}".format(\
#         name, location, damage))
#
# attack(name, "1h", damage)

class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# marine1 = Unit("marine", 40, 5)
# marine2 = Unit("marine", 40, 5)
# tank = Unit("tank", 150, 5)

#Wraith
# wraith1 = Unit("wraith", 80, 5)
# print("name : {0}, damage : {1}".format(wraith1.name, wraith1.damage))
#
#
# #Mind control
# wraith2 = Unit("wraith", 80, 5)
# wraith2.clocking = True
#
# if wraith2.clocking == True:
#     print("{0} is under clocking".format(wraith2.name))

class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} attack damage {2}".format(self.name, location, self.damage))

    def damaged(self, damage):
        self.hp -= damage
        if self.hp <=0:
            print("{0} : died".format(self.name))


# firebat1 = AttackUnit("firebat", 50, 16)
# firebat1.attack("5h")
#
# firebat1.damaged(25)
# firebat1.damaged(25)

#Flying class
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} direction speed {2}"\
            .format(name, location, self.flying_speed))

#Flyable attack class
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)


valkyrie= FlyableAttackUnit("valkyrie", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3h")
