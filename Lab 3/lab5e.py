'''
Name: Aritra Nandy

Student ID: 137916227

 '''

import sys

 

def is_number(s):

    try:

        int(s)

        return True

    except ValueError:

        return False

 

def main():

    # Check if there are no command line arguments

    if len(sys.argv) == 1:

        print("Usage: Enter one or more command line arguments.")

        sys.exit(1)

 

    numbers = []

    for arg in sys.argv[1:]:

        if is_number(arg):

            numbers.append(int(arg))

            print(f"Number found: {arg}.")

        else:

            print(f"Error: {arg} is not a number.")

 

    if numbers:

        average = sum(numbers) / len(numbers)

        print(f"Average for {len(numbers)} numbers: {average:.1f}")

 

if __name__ == "__main__":

    main()