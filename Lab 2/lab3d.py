'''
Name: Aritra Nandy
Student ID : 137916227
description  : Lab3d
'''
from random import randint
secret_number = randint(1,10)
user_input = int(input("Guess a number between 1 and 10 :"))
while user_input !=secret_number:
    if user_input !=secret_number:
        print("Sorry, that's not it")
        user_input=int(input("Guess a number between 1 and 10"))

print("Correct! You win")

