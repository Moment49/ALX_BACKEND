# class Dog:
#     """A class that models a real life dog"""

#     def __init__(self, name, age):
#         # Public access data
#         self.name = name
#         self.age = age
    
#     def display_dog(self):
#         print(f"This is the name of my dog {self.name} and he is {self.age} old")
    
# dog1 = Dog("charlie", 7)

# dog1.display_dog()
# # finding all the fields and methods which are present inside dog1
# print("List of fields and methods inside obj:", dir(dog1))

# class Cat:
#     """Model a cat"""
#     # protected data members
#     _name = None
#     _color = None
    
#     def __init__(self, name, color) -> None:
#         self._name = name
#         self._color = color
    
#     def _display(self):
#         print(f"Name: {self._name} and Color: {self._color}")

# class Meow(Cat):
#     """Model cat sound"""
#     def __init__(self, name, color):
#         super().__init__(name, color)
    
#     def bark(self):
#         print (f" The cat {self._name} meows and its color is {self._color}")
        
#         self._display()


# cat1 = Cat('muffy', 'black')
# cat1._display()
# print(cat1.name)

# m1 = Meow("puffy", 'white')
# m1.bark()
