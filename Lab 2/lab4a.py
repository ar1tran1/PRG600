'''
Name: Aritra Nandy
Student ID : 137916227
description  : Lab4a
'''
import random

def guess_number():
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)

    while True:
        try:
            # Get user input
            guess = int(input("Enter a number between 1 and 10: "))

            # Check if the guess is within the valid range
            if 1 < guess < 10:
                if guess == secret_number:
                    print("Correct! You win")
                    break
                else:
                    print("Sorry, Try again.")
            else:
                print("Error: not a number or out of bounds")

        except ValueError:
            print("Error: Not a number or out of bounds")

if __name__ == "__main__":
    guess_number()


