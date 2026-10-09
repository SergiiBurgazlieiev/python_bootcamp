import random

# Generate a random integer
# random_integer = random.randint(1, 10)
# print(random_integer)

# Generate a random float between 0 and 1
# random_number_0_to_1 = random.random()
# print(random_number_0_to_1)

# Generate a random float within a range
# random_float = random.uniform(10, 20)
# print(random_float)

# Heads or tails
# random_heads_or_tails = random.randint(0, 1)

# if random_heads_or_tails == 0:
#     print("Heads")
# else:
#     print("Tails")


# Python lists

# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# random_friend = random.randint(0, 4)
# print(friends[random_friend])
# print(random.choice(friends))


# Final Project - Rock Paper Scissors

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

symbols = [rock, paper, scissors]

user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:\n")
)

if user_choice < 0 or user_choice >= 3:
    print("You typed an invalid number. You lost!")
else:
    # Display the user's choice
    print(symbols[user_choice])

    # Generate and display the computer's choice
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(symbols[computer_choice])

    # Compare choices and determine the winner
    if (
        (computer_choice == 0 and user_choice == 2)
        or (computer_choice == 2 and user_choice == 1)
        or (computer_choice == 1 and user_choice == 0)
    ):
        print("You lost!")
    elif computer_choice == user_choice:
        print("It is a tie! Try one more time!")
    else:
        print("You win!")