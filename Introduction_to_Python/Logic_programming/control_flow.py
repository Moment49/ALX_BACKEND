# Control Flow

# name = "Alx"
# age = 120

# print(age)

# if age >= 50:
#     print("You have access")
# else:
#     print("You don't have access")

# condition = age = 10
# condtion_2 = 'frontend' == 'backend'
# print(condtion_2)
# print(age)

# email = input("Enter your email: ")
# correct_email = "be@alx.com"

# while email != correct_email:
#     email = input("Enter your email: ")

# print("Success")
    # if email == correct_email:
    #     print("You have access")
    #     break
    # else:
    #     print("Access denied")

# Iterating  -> going over 
# Sequence -> Strings, lists, tuples
# name = "alx"
# for n in name:
#     print(n)

# for a in range(len(name)):
#     print(name[a])

# for x in enumerate(name):
#     print(x)
# nums = [x for x in range(1, 4)]
# print(nums)

# Match Statements
# n = 10
# match n:
#     case 4:
#         print("not c orrect number")
#     case 2:
#         print("Correct num")
#     case _:
#         print("Simple number")

# day = input("What day of the week is it?: ").lower()

# match day:
#     case 'monday':
#         print("Ugh..Its monday")
#     case "tuesday":
#         print("Another workday")
#     case "wednesday":
#         print("Thank God is Wednesday")
#     case "Thursday":
#         print("Still a workday")
#     case "Friday":
#         print("TGIF")
#     case "saturday" | "sunday":
#         print("Its a weekend")
#     case _:
#         print("Thats not part of the week")

# Matching DATA Types
# value = input("Enter a value (number or string): ")

# match value:
#     case int():
#         print("Its a number / Integer")
#     case str():
#         print("Its a string")
#     case float():
#         print("Its a floating number")
#     case bool():
#         print("Its a boolean")
#     case _:
#         print("can be any data type")

# age = int(input("Enter your age: "))
# voting_id = True

# match age:
#     case age if age >= 18:
#         if voting_id:
#             print("You have a voting right")
#         else:
#             print("You need a voting ID")
#     case _:
#         print("You are not eligbile to vote")

# Matching Lists

# def greeting(details):
#     match details:
#         case [time, name]:
#             return f"{time}, {name}"
#         case [time, *names]:
#             names_str = ''
#             for name in names:
#                 names_str+=f"{time} {name}\n"
#             return names_str
#         case _:
#             return 'Emtpy List nobody to greet'


# greet = greeting(['Good evening', 'Elvis', 'Dave', 'Mike'])
# print(greet)

# def fruit_get(*args):
#     for arg in args:
#         print(arg)
#     print(args)

# fruit_get(1, 2, 3)

# def fruit_gets(**fruit_salad):
#     fruit_salad['fruit_crusher'] = 'blender'
#     return fruit_salad

# make_fruit = fruit_gets(fruit_type="orange")
# print(make_fruit)

# LOOPS
# fruits = ['bananas', 'oranges', 'apples']

# for fruit in fruits:
#     print(fruit)

# # Iterating through a tuple
# colors = ("red", 'green','blue')
# for color in colors:
#     print(color)

# Iterating through arange
# for x in range(1, 6):
#     print(x)

# for num in range(1, 10, 2):
#     print("Sending Email", num  * ".")

# success = False
# for mail_attept in range(3):
#     print("email attempt")
#     if success:
#         print("Mail successfully sent..")
#         break
# else:
#     print("Attepted 3 times to send email")

# Nested LOOPS
# for x in range(4):
#     for y in range(3):
#         print(f"({x}, {y})")

# Program to print number from 1 - 10
# count = 0
# for num in range(1, 10):
#     if num % 2 == 0:
#         print(num)
#         count+=1
# print(f"We have {count} even numbers")

# Chanllenge 3 - 
# Numbers can add up quickly! Write a Python program using a for loop to calculate the sum of all the numbers in a list.

# Create a list of numbers (e.g., numbers = [1, 5, 3, 9]).
# Initialize a variable total to 0, which will store the running sum.
# Use a for loop to iterate over the numbers list.
# Inside the loop, add the current number (use the loop variable) to the total variable.
# After the loop, print the final total value, which represents the sum of all the numbers in the list

# Program/Solution
# numbers = [1, 5, 3, 9]
# total = 0
# for number in numbers:
#     total += number
# print(f"The sum total of the numbers in the list is: {total} ")

# While Loops
# user_age = int(input("What's your age: "))

# while user_age < 18:
#     user_age = int(input("Enter age (You must be 18 and above to proceed): "))

# print("You are old enough")

# Guess number
# secret_num = 7

# guess_count = 0
# guess = 0

# while guess != secret_num:
#     guess = int(input("Guess a number between 1 and 10: "))
#     guess_count += 1

# print(f"You guessed right the correct number: {secret_num} and your attempts: {guess_count}")

#Iterating Until a Specific Condition:
# shopping_cart = ['Orange', 'milk', 'tea']
# item_found = False

# while not item_found:
#     item = input("Please enter the item to see if its in your shopping cart: ")
#     if item in shopping_cart:
#         print("Item found")
#         item_found = True
#     else:
#         print(f"The item {item} is not on the shopping cart")

# NESTED WHILE LOOPS

# outer_count = 5

# while outer_count > 0:
#     # Outer loop controls the number of times the inner loop runs
#     inner_count = 1
#     while inner_count <= outer_count:
#         # Inner loop repeats for each outer loop iteration
#         print(inner_count, end=" ")
#         inner_count += 1
#     print()  # Move to a new line after each outer loop iteration
#     outer_count -= 1

# Multiplication table
for i in range(1, 11):
  # Outer loop iterates through rows (multiplication factors)
  for j in range(1, 11):
    # Inner loop iterates through columns (other factors)
    product = i * j
    print(f"{i} x {j} = {product}", end="\t")  # Print with tabs for better formatting
  print()  # Move to a new line after each row

i = 1
while i <= 12:
    j = 1
    while j <= 12:
        product = i * j
        print(f"{i} x {j} = {product}", end="")
        j += 1
        print()
    i += 1













