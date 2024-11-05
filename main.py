
class Vehicle:
    def __init__(self, name, maxspeed, mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage

    def display_info(self):
        print("Vehicle Name:", self.name)
        print("Max Speed:", self.maxspeed, "km/h")
        print("Mileage:", self.mileage, "km/l")


class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, fare_per_passenger):
        super().__init__(name, max_speed, mileage)
        self.fareperpassenger = fare_per_passenger

    def calculate_total_fare(self, numberofpassengers):
        return numberofpassengers * self.fareperpassenger


schoolbus = Bus("School Volvo", 180, 12, 5)


schoolbus.display_info()


numberofpassengers = 20
totalfare = schoolbus.calculate_total_fare(numberofpassengers)
print("Total fare for", numberofpassengers, "passengers:", totalfare)
