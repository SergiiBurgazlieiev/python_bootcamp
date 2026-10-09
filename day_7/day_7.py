import random

import hangman_art
import hangman_words

lives = 6
guessed_letters = set()

chosen_word = random.choice(hangman_words.word_list)
blanks = ["_"] * len(chosen_word)

print(f"{hangman_art.logo3}\n")
print(f'Word to guess: {"".join(blanks)}\n')

while lives > 0 and "_" in blanks:
    print(f"You have {lives} lives left.\n")

    guess = input("Please guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    if guess in guessed_letters:
        print(f"You have already guessed '{guess}'.")
        continue

    guessed_letters.add(guess)

    if guess in chosen_word:
        for index, char in enumerate(chosen_word):
            if char == guess:
                blanks[index] = guess
    else:
        lives -= 1
        print(f"'{guess}' is not in the word. You lose a life.")

    print("".join(blanks))
    print(hangman_art.stages[lives])

if "_" not in blanks:
    print("You won!")
else:
    print(f"You lose! The word was '{chosen_word}'.")