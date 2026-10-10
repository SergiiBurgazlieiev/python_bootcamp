import art

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

print(art.logo)


def caesar(original_text, shift_amount, shift_direction):
    final_result = ""

    # If the user wants to decode, reverse the shift direction
    # by making the shift amount negative.
    if shift_direction == "decode":
        shift_amount *= -1

    for char in original_text:
        if char.isalpha():
            index_of_char = alphabet.index(char)
            # Calculate the new position after applying the shift.
            # % len(alphabet) makes the index wrap around.
            # Example: "z" shifted by 1 becomes "a".
            new_index = (index_of_char + shift_amount) % len(alphabet)
            final_result += alphabet[new_index]
        else:
            final_result += char

    print(f"Here is the {shift_direction}d result: {final_result}")


run_program = True

while run_program:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n"
    ).lower()

    text = input("Type your message:\n").lower()

    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    continue_game = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'\n"
    ).lower()

    if continue_game == "no":
        run_program = False
        print("The game is over!")