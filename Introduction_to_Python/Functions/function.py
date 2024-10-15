# def greet(name):
#     """Prints a greeting message"""
#     print(f"Hello", {name})

# # Lambda
# add = lambda x, y: x + y

# result = add(5, 3)
# print(result)

# Variable Scope (Local and Global Scope)
# Variable defined inside the function are called local scope
# While variables defined outside func are called gloabl scope

# count = 0  #Global variable

# def increment():
#     global count
#     count += 1


# increment()
# print(count)

# Nested Functions
# def outer_function():
#     x = 10 #var in enclosing func

#     def inner_function():
#         nonlocal x
#         x += 5 
#         print(x)

#     inner_function()
# outer_function()



# Exercise 1, 2 and 3

# Data Structures
# my_list = [10, 20, 30, 40, 50]

# print(my_list[2])

# # Slice
# print(my_list[0: 4: 2])
# print(my_list[::-1])

# Sets
# a = {3, 4, 5,6}
# b = {4, 5, 6, 7, 8} 
# print(a.intersection(b))
# print(a.union(b))
# print(b.difference(a))

# Python Libraries/Packages
# A module is a python file containing all functions, variables and classes
# While a package is a directory containing multiple modules and subdirectories(more packages)

# import os #Module  for interacting with the operating system

# # Get the current working directory
# cwd = os.getcwd()
# print(cwd)

# count = 10  # Global variable

# def outer_function():
#   count = 5  # Local variable within outer_function

#   def inner_function():
#     count = 2  # Local variable within inner_function
#     print(f"Inner function: {count}")  # Accesses local count (2)

#   inner_function()
#   print(f"Outer function: {count}")  # Accesses local count (5)

# print(f"Global scope: {count}")  # Accesses global count (10)

# outer_function()


import builtins

# print(dir(builtins))










