import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print("Welcome to Bagels!")
    print(f"I am thinking of a {NUM_DIGITS}-digit number. Try to guess what it is.")
    print("Here are some clues:")
    print("When I say:    That means:")
    print("  Pico         One digit is correct but in the wrong position.")
    print("  Fermi        One digit is correct and in the right position.")
    print("  Bagels       No digit is correct.")
    print(f"You have {MAX_GUESSES} guesses to get it right.\n")

    while True:
        secret_num = get_secret_num()
        print("I have thought up a number.")
        print(f"You have {MAX_GUESSES} guesses to get it.")

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{num_guesses}: ")
                guess = input().strip()

            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break
            if num_guesses > MAX_GUESSES:
                print(f"You've run out of guesses. The answer was {secret_num}.")

        print("Do you want to play again? (yes or no)")
        if not input().lower().startswith('y'):
            break
    print("Thanks for playing!")


def get_secret_num():
    """Returns a string made upt of NUM_DIGITS unique random digits."""
    numbers = list('0123456789')  # Create a list of digits 0-9.
    random.shuffle(numbers)  # Shuffle them into random order.

    # Get the first NUM_DIGITS digits in the list for the secret number.
    secret_num = ''
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num


def get_clues(guess, secret_num):
    """Returns a string with the pico, fermi, bagels clues for a guess and secret number pair."""
    if guess == secret_num:
        return "You got it!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            # A correct digit in the correct place.
            clues.append("Fermi")
        elif guess[i] in secret_num:
            # A correct digit in the wrong place.
            clues.append("Pico")

    if len(clues) == 0:
        return "Bagels"  # There are no correct digits at all.
    else:
        # Sort the clues into alphabetical order so their order doesn't give information away.
        clues.sort()
        # Make a single string from the list of clues.
        return ' '.join(clues)
    

if __name__ == "__main__":
    main()