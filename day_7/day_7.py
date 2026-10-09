import random

import hangman_art
import hangman_words

game_over = False
lives = 6
blanks = []
guessed_letters = set()

print(f"{hangman_art.logo3}\n")

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

for _ in range(word_length):
    blanks.append("_")

print(f'Word to guess: {"".join(blanks)}\n')

while not game_over:
    print(f"**************************** You have {lives} lives left ****************************\n")

    guess = input("Please guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You have already guessed {guess}")
        continue

    guessed_letters.add(guess)

    if guess in chosen_word:
        for index, char in enumerate(chosen_word):
            if char == guess:
                blanks[index] = char
    else:
        lives -= 1
        print(f"You guessed '{guess}', which is not in the word. You lose a life.")

    print("".join(blanks))
    print(hangman_art.stages[lives])

    if "_" not in blanks:
        game_over = True
        print("You won!")
    elif lives == 0:
        game_over = True
        print("You lose!")