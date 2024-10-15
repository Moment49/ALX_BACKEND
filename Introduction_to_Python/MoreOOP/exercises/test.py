# Exercise 1
class Shape:
    """A class to model a shape"""
    def calculate_area(self):
        print("Calculate the area of a rectangle")

class Rectangle(Shape):
    def calculate_area(self, x, y):
        print(f"Area of Rectangle: {x * y}")


area_rect = Rectangle()
area_rect.calculate_area(3, 4)

# Exercise2
class Bird:
    def fly(self):
        print("A bird can fly")
    def run(self):
        print("A mammal can run")

class Mammal:
    def run(self):
        print("A mammal can run")
    def fly(self):
        print("A bird can fly")


class Bat(Bird, Mammal):
    def fly(self):
        print("The bat can fly")

    def run(self):
        print("A bat can run")



test_bat = Bat()
test_bat.run()
test_bat.fly()

class Dog:
    def make_sound(self):
        print("Woof!!!!")

class Cat:
    def make_sound(self):
        print("Meow!!!")

class Bird:
    def make_sound(self):
        print("Whistle!!!")

animal_obj = [Dog(), Cat(), Bird()]

def let_them_speak(ani_objs):
    for ani_obj in ani_objs:
        ani_obj.make_sound()

let_them_speak(animal_obj)