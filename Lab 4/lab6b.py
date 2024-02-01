'''
Name: Aritra Nandy
ID : 137916227/anandy
Description : Lab6b
'''

import sys

# Check if a filename is provided as a command-line argument
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = 'readme.txt'  # Default filename if no argument is provided

try:
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines.reverse()  # Reverse the order of lines

        for line in lines:
            print(line.rstrip())  # Print each line, removing trailing newline character
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")