import random

# Find the highest score manually
# student_scores = [180, 124, 165, 173, 189, 169, 146]

# max_score = 0

# for score in student_scores:
#     if max_score < score:
#         max_score = score

# print(max_score)


# range() with a for loop

# for number in range(1, 11):
#     print(number)


# Add numbers from 1 to 100

# total = 0

# for number in range(1, 101):
#     total += number

# print(total)


# Final Project - PyPassword Generator

characters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z"
]

numbers = [
    "0", "1", "2", "3", "4",
    "5", "6", "7", "8", "9"
]

symbols = [
    "!", "@", "#", "$", "%", "^", "&", "*",
    "(", ")", "-", "_", "=", "+",
    "[", "]", "{", "}", "|",
    ":", ";", "'", ",", ".",
    "<", ">", "?", "`", "~"
]

password_list = []

print("Welcome to the PyPassword Generator!")

number_letters = int(
    input("How many letters would you like in your password?\n")
)

number_symbols = int(
    input("How many symbols would you like?\n")
)

number_numbers = int(
    input("How many numbers would you like?\n")
)

# Add random letters
for _ in range(number_letters):
    char = random.choice(characters)
    password_list.append(char)

# Add random symbols
for _ in range(number_symbols):
    symbol = random.choice(symbols)
    password_list.append(symbol)

# Add random numbers
for _ in range(number_numbers):
    number = random.choice(numbers)
    password_list.append(number)

# Shuffle the password characters
random.shuffle(password_list)

# Convert the list into a string
password = "".join(password_list)

print(f"Here is your password: {password}")