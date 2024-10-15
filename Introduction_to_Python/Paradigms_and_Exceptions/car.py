class Car:
    """A class to model a real world car"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #Default reading for odometer
    
    def get_descriptive_name(self):
        full_name = f"{self.year} {self.make} {self.model}"
        return full_name

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

my_car = Car('Toyota', 'Venza', 2024)

car_desc = my_car.get_descriptive_name()
print(car_desc)

my_car.read_odometer()
my_car.update_odometer(200)
my_car.read_odometer()

my_car.increment_odometer(50)
my_car.read_odometer()

print(my_car.model)