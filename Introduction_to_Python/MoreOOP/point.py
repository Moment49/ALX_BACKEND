# # Constructors (__init__)
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


# # Create a Point Object
# point = Point(3, 5)
# print(f"Point coordinates: ({point.x}, {point.y})")


# # Destructors (__del__)

# class FileHandler:
#     def __init__(self, filename):
#         self.filename = filename
#         # Reads the file
#         self.file_ = open(self.filename, 'r')

#     def read_data(self):
#         return self.file_.read()
    
#     def __del__(self):
#         self.file_.close()

# from pathlib import Path

# file_name = Path('shell/fruits.txt')

# file_obj = FileHandler(file_name)

# print(file_obj.read_data())


# Magic Methods
# __str__ : Defines how an object is represented as a string
# __repr__ : Defines the official string representation of an object

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __str__(self) -> str:
#         return f"Name: {self.name}, Age: {self.age}"

# person = Person('Alice', 30)
# print(person)

# Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def make_sound(self):
        print("Woof")

# dog = Dog('Buddy', 'German sherphard')
# dog.make_sound()

# Multiple Inheritance
# class Flyer:
#     def fly(self):
#         print("Flying...")

# class Swimmer:
#     def swim(self):
#         print("Swimming...")

# class Duck(Flyer, Swimmer):
#     pass

# duck  = Duck()
# duck.fly()
# duck.swim()

# Multilevel Inheritance
# class Vehicle:
#     def move(self):
#         print("Moving...")

# class Car(Vehicle):
#     pass

# class ElectricCar(Car):
#     def charge(self):
#         print("Charging...")


# tesla = ElectricCar()
# tesla.move()
# tesla.charge()


# Composition as an Alternative
# class Car:
#     def __init__(self, engine):
#         self.engine = engine
    
#     def start(self):
#         self.engine.start()

# class Engine:
#     def start(self):
#         print("Engine starting.....")

# engine = Engine()

# car = Car(engine)
# car.start()

# Understanding MRO (Method Resolution Order)
class A:
    def greet(self):
        return "Hello from class A"

class B(A):
    def greet(self):
        return "Hello from class B"

class C(A):
    def greet(self):
        return "Hello from class C"

class D(B, C):
    pass

# creating an instance of class D
obj_d = D()
print(obj_d.greet())

# Polymorphism
class Animal:
    def make_sound(self):
        print("General animal sound")


class Dog(Animal):
    def make_sound(self):
        print("Woof!")

animals = [Dog(), Animal()]

for animal in animals:
    animal.make_sound()