# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("You are not allowed to ride!")


# Operators

# Modulo operator %
# num = int(input("Enter your number here: "))

# if num % 2 == 0:
#     print("Number is even")
# else:
#     print("Number is odd")


# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")

# bill = 0

# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25

# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is: ${bill}")


# Final Project - Treasure Island

print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

step_1 = input(
    'You\'re at a crossroads. Where do you want to go?\n'
    'Type "left" or "right"\n'
).lower()

if step_1 == "left":
    step_2 = input(
        "You have come to a lake. "
        "There is an island in the middle of the lake. "
        'Type "wait" to wait for a boat or "swim" to swim across.\n'
    ).lower()

    if step_2 == "wait":
        step_3 = input(
            "You arrived at the island unharmed. "
            "There are three doors. Choose a door! "
            'Type "red", "blue", or "yellow"\n'
        ).lower()

        if step_3 == "red":
            print("Burned by fire. Game Over.")
        elif step_3 == "blue":
            print("Eaten by beasts. Game Over.")
        elif step_3 == "yellow":
            print("You Win!")
        else:
            print("Game Over!")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fell into a hole. Game Over.")