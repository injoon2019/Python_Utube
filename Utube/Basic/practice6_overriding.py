class Unit:
  def __init__(self, name, hp, speed):
    self.name = name
    self.hp = hp
    self.speed = speed

  def move(self, location):
    print("move")
    print("{0} : {1} move speed {2}"\
        .format(self.name, location, self.speed))

#Attack Unit
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0}, {1}".format(self.name, location))

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1}, {2}".format(name, \
        location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("flyable unit move")
        self.fly(self.name, location)


vulture = AttackUnit("vulture:", 80, 10 ,20)

battlecruiser = FlyableAttackUnit("BattleCruiser", 500, 25, 3)

vulture.move("11h")
battlecruiser.move("9h")

#Building
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)
        self.location = location


supply_depot = BuildingUnit("Supplt depot", 500, "7h")


def game_start():
    print("new game start")

def game_over():
    pass
