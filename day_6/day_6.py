# Day 6 - Functions, While Loops, and Reeborg's World

# Python built-in functions:
# https://docs.python.org/3/library/functions.html


# Define a simple function
def greet():
    print("Hello!")


greet()


# Function with a parameter
def greet_user(name):
    print(f"Hello, {name}!")


greet_user("Sergii")


# Reeborg's World helper function:
# Turn right by turning left three times.
#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# Reeborg's World maze logic:
#
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()


# Key concepts:
# - Define reusable functions with def
# - Call functions by using their name followed by ()
# - Use while loops when the number of repetitions is unknown
# - Use conditions to control loop behavior
# - Break larger problems into smaller reusable functions