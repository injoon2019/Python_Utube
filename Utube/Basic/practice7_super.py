class Unit:
    def __init__(self):
        print("Unit")

class Flyable:
    def __init__(self):
        print("Flyable")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        #super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

#Dropship
dropship = FlyableUnit()

#Quiz
class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    #Info
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, \
            self.completion_year)


houses = []
house1 = House("Gangnam", "apt", "sell", "10", "2010")
house2 = House("Mapo", "office", "jeonse", "5", "2007")
house3 = House("Songpa", "billa", "wolse", "500/50", "2000")
houses.append(house1)
houses.append(house2)
houses.append(house3)

print("{0} houses".format(len(houses)))
for house in houses:
    house.show_detail()
