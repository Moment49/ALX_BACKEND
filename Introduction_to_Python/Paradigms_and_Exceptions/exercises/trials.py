# Exercise 1
# class Student:
#     """A class to model a student in a classroom"""
#     def __init__(self, name, age):
#         """Initialize the attributes of the student"""
#         self.name = name
#         self.age = age

#     def student_info(self):
#         """Display student information"""
#         return f"The name of the student is {self.name} and the age is {self.age}"


# student_1 = Student("Elvis Ibenacho", 27)
# student_info = student_1.student_info()
# print(student_info)

# Exercise 2
# class Product:
#     """A class to model a product of an item"""
#     def __init__(self, name, price, quantity):
#         """Initialize an attribute of the product"""
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def calculate_product_stock(self):
#         total_product_cost = self.price * self.quantity
#         return total_product_cost

# product_1 = Product("Jeans", 30, 5)
# total_stock_val = f"The total value of the product in stock is {product_1.calculate_product_stock()}"
# print(total_stock_val)

# Exercise 3
# Write a program that takes two numbers as input from the user and divides the first number by the second number.
# Handle the ZeroDivisionError exception to inform the user if they attempt to divide by zero.

# class Division:
#     """A model a division of numbers"""
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
    
#     def validate_exception(self):
#         try:
#             result = self.num1/self.num2
#         except ZeroDivisionError:
#             return f"Cannot divide number by zero"
#         else:
#             return result


# num1 = int(input("Num1: "))
# num2 = int(input("Num2: "))

# num_division = Division(num1, num2)
# result = num_division.validate_exception()
# print(result)

# Exercise 3
# from pathlib import Path

# p = Path('shell/fruits.txt')
# # print(p.absolute())
# file_name = p.absolute()
# print(file_name)


# try:
#     with open(file_name) as f:
#         read_file = f.read()
#         print(read_file)
# except FileNotFoundError:
#     print("File not found are you sure file exists")

# Exercise 4
# class ValueTooHighError(Exception):
#     """A class to model a custome Value Exception"""
#     def __init__(self, number):
#         self.number = number

#     def __str__(self):
#         return f"The number {self.number} is too high"


# try:
#     num = int(input("Enter number: "))
#     if num > 100:
#         raise ValueTooHighError(num)
#     else:
#         print(f"{num} is within the approriate range")
# except ValueError:
#     print("Value must be a number")


# Write a small Python function (e.g., a function to calculate the square of a number) 
# and intentionally introduce a bug (e.g., incorrect calculation logic).

import unittest

def square_num(number):
    return number*number + 1


class SquareTest(unittest.TestCase):
    """Test class for the numbers to be squared"""

    def test_valid_square(self):
        result = square_num(5)
        self.assertEqual(result, 26)

    def test_invalid_square(self):
        result = square_num(5)
        self.assertNotEqual(result, 25)

   


if __name__ == "__main__":
    unittest.main()


