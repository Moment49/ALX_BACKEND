name  = "Hello World"
print(name)

result = 10 + 5 #Addition: result will be 15
difference = 20 - 7 #Substraction: result will be 13
product = 4 * 3 #multiplication: result will be 12
divide = 10 / 4 
print(divide)

reminder = 10 % 3
print(reminder)

is_greater = 10 % 5 != 0
print(is_greater)

is_eqiv = 10 == '10'
print(is_eqiv)

# Type casting
age_in_string = "34"  # This is a string, not a number

# We can convert the string to an integer using int() for calculations
age_in_numbers = int(age_in_string)  # Now age_in_numbers is 25 (integer)
print(age_in_numbers)

# Be cautious during type casting, it might not always be successful! 
# For example, trying to convert "hello" to an integer will result in an error.

# User Input
# User Input 
# name = input("What is your name?: ")
# print(f"Hello, {name}")

num1 = int(input("Enter the first number: "))  # Convert input to integer
num2 = int(input("Enter the second number: "))

# Perform the addition and store the result
sum = num1 + num2

print("The sum of", num1, "and", num2, "is", sum)

# COMMENTS
# How to Write Effective Comments:
# Clarity and Conciseness: Strive for clear and concise comments that accurately explain the code’s purpose. 
# Avoid overly complex explanations or restating the obvious code.

# Explain the “Why”:Focus on explaining the “why” behind your code choices. 
# Don’t just describe what the code does; explain the reasoning and logic that led to that implementation.

# Document Assumptions: If your code relies on specific assumptions about data or external factors, document those assumptions clearly in comments.
# Use Consistent Style: Maintain a consistent commenting style throughout your code. 
# This improves readability and makes your code easier to navigate for anyone who encounters it.

# Example
# Loop through a list of exam scores and print grades based on a specific grading scale.
grades = [85, 92, 78, 99, 65]
for score in grades:
  if score >= 90:
    print(score, "is an A.")
  elif score >= 80:
    print(score, "is a B.")
