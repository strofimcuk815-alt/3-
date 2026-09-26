class Human:
    def __init__(self, name="Human"):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)

    def print_passengers_names(self):
        if self.passengers != []:
            print(f"Names of {self.brand} passengers: ")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"There are no passenger in {self.brand}")
class Plane:
    def __init__(self, plane):
        self.plane = plane
        self.passenger = []

    def add_passenger(self, human):
        self.passenger.append(human)

    def print_passenger_names(self):
        if self.passenger != []:
            print(f"Names of {self.plane} passenger: ")
            for passenger in self.passenger:
                print(passenger.name)
        else:
            print(f"There are no passenger in {self.plane}")

nick = Human("Nick")
kate = Human("Kate")
rick = Human("Rick")
lily = Human("Lily")
car = Auto("Mercedes")
plane = Plane("Mriya")

car.add_passenger(nick)
car.add_passenger(kate)
plane.add_passenger(rick)
plane.add_passenger(lily)

plane.print_passenger_names()
car.print_passengers_names()