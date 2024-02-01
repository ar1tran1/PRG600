'''
Name: Aritra Nandy
ID : 137916227/anandy
Description : Lab6c
'''

import sys

if len(sys.argv) != 3: # Checks if the number of command-line arguments is not equal to 3
    print("Usage: lab6c.py keyword filename") # Prints usage instructions if arguments are incorrect
else:
    keyword = sys.argv[1] # Gets the keyword from the first command-line argument
    filename = sys.argv[2] # Gets the filename from the second command-line argument
    try:
        with open(filename, 'r') as f: # Opens the specified file for reading
            lines = f.readlines() # Reads all the lines from the file into a list
        
        
        for linenumber, line in enumerate(lines,1): # Iterate through each line in the list, keeping track of line numbers starting from 1
            if keyword in line: # Check if the keyword is in the current line
                print(f"{linenumber}: {line.strip()}") # If found, print the line number and the line (stripped of leading/trailing spaces and newlines)
    except FileNotFoundError:
        print(f"ERROR: {filename} not found.") # Handles the case where the file is not found and print an error message
        sys.exit(1) # Exits the program with an error code of 1