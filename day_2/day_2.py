# Data Types in Python

# String
# print("Hello"[-1])

# Integer - whole number
# print(123 + 345)

# Large integers can use underscores for readability
# print(123_456_789)

# Float - floating-point number
# print(3.14)

# Boolean - True or False
# print(True)
# print(False)

# Check the type of a value with type()
# print(type(123))
# print(type("string"))
# print(type(3.14))
# print(type(True))

# Type conversion / type casting
# int(), float(), str(), bool()
# number = int("123")
# print(type(number))

# Convert values when combining different data types
# print("Number of letters in your name: " + str(len(input("Enter your name:\n"))))

# Math operations
# print(123 + 456)
# print(7 - 3)
# print(3 + 6)
# print(10 / 2)   # Division returns a float: 5.0
# print(10 // 2)  # Floor division returns 5
# print(2 ** 2)   # Exponent: 2 to the power of 2

# PEMDAS - order of mathematical operations
# Parentheses, Exponents, Multiplication/Division, Addition/Subtraction

# Example
# print(3 * 3 + 3 / 3 - 3)

# Parentheses can change the order of operations
# print(3 * (3 + 3 / 3 - 3))

# BMI calculation
# bmi = 84 / 1.65 ** 2
# print(bmi)
# print(int(bmi))
# print(round(bmi, 2))

# Assignment operators
# score = 0
# score += 1
# score -= 1

# f-strings
# score = 0
# height = 1.8
# is_winning = True

# print(
#     f"Your score is {score}, your height is {height}, "
#     f"and you are winning: {is_winning}"
# )

# Final Project - Tip Calculator

print("Welcome to the tip calculator!")

total = float(input("What was the total bill? $\n"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
people_count = int(input("How many people to split the bill?\n"))

total_after_tip = total + (tip / 100 * total)
total_for_each_person = total_after_tip / people_count
final_bill_per_person = round(total_for_each_person, 2)

print(f"Each person should pay: ${final_bill_per_person}")