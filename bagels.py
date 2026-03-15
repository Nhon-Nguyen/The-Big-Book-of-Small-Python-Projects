import random

# Configuration Constants
NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    """
    Main game loop for Bagels. 
    Handles the introduction, game initialization, and play-again logic.
    """
    show_instructions()

    while True:
        secret_num = get_secret_num()
        print("\nI have thought up a number.")
        print(f"You have {MAX_GUESSES} guesses to get it.")

        game_won = play_round(secret_num)

        if not game_won:
            print(f"You've run out of guesses. The answer was {secret_num}.")

        print("\nDo you want to play again? (yes/no)")
        if not input("> ").lower().startswith('y'):
            break
            
    print("Thanks for playing!")

def show_instructions():
    """Prints the game rules and clue definitions to the console."""
    instructions = f"""
Welcome to Bagels!
I am thinking of a {NUM_DIGITS}-digit number with no repeating digits.
Try to guess what it is. Here are some clues:

When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.
    """
    print(instructions)

def get_secret_num():
    """
    Generates a string of unique random digits.
    
    Returns:
        str: A string of length NUM_DIGITS containing unique digits 0-9.
    """
    numbers = list('0123456789')
    random.shuffle(numbers)
    return ''.join(numbers[:NUM_DIGITS])

def get_clues(guess, secret_num):
    """
    Determines the Pico, Fermi, or Bagels clues for a given guess.
    
    Args:
        guess (str): The user's input string.
        secret_num (str): The target number string.
        
    Returns:
        str: A space-separated string of clues, sorted alphabetically.
    """
    if guess == secret_num:
        return "You got it!"

    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append("Fermi")
        elif guess[i] in secret_num:
            clues.append("Pico")

    if not clues:
        return "Bagels"
    
    clues.sort()
    return ' '.join(clues)

def play_round(secret_num):
    """
    Handles the guessing logic for a single round of the game.
    
    Returns:
        bool: True if the user guessed the number, False otherwise.
    """
    for num_guesses in range(1, MAX_GUESSES + 1):
        guess = ""
        # Validation Loop
        while len(guess) != NUM_DIGITS or not guess.isdecimal():
            print(f"Guess #{num_guesses}:")
            guess = input("> ").strip()

        clues = get_clues(guess, secret_num)
        print(clues)

        if guess == secret_num:
            return True
            
    return False

if __name__ == "__main__":
    main()