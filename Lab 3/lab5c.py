'''

Name: Aritra

Student ID: 137916227

Lab5c.py to select random animal based on single letter from the animals list

 

'''

 

from random import randint

 

animals = ['snake', 'hamster', 'scorpion', 'beaver', 'mosquito', 'camel', 'vulture', 'horse', 'python', 'capybara'] #copying the animals into list

 

# Select a random word from the animals list

secret_animal = randint(0, len(animals) - 1)

secret = animals[secret_animal]

 

print("I'm thinking of an animal. Can you guess what it is?")

 

# Initialize a set to store guessed letters

guessed_letters = set()

 

# while loop

while True:

    user_guess = input("Enter a letter or a guess. Press enter to quit: ").lower()

 

    # Check if the user pressed Enter without any guess

   # if user_guess == "":

        #break

 

    if len(user_guess) == 1 and user_guess.isalpha():

        # Check if the guess is a single letter

        if user_guess in guessed_letters:

            print("You already guessed that letter.")

        elif user_guess in secret:

            print("Yes, my word contains that letter.")

            guessed_letters.add(user_guess)

        else:

            print("Sorry, my word doesn't contain that letter.")

            guessed_letters.add(user_guess)

    elif user_guess == secret:

        print("You win!")

        break

    else:

        print("Sorry, that's not it.")

 

       

'''

# Print the secret word if the user didn't guess it

if guess != secret:

    print(f"The secret word was '{secret}'.")

'''