'''
Name: Aritra Nandy
ID : 137916227/anandy
Description : Lab6d
'''


import sys

# Check if a filename is provided as a command line argument
if len(sys.argv) != 2:
    print("Usage: lab6d.py <filename>")
else:
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file: # Open file in read mode and save contents to lines list with readlines()
            lines = file.readlines()

        
        with open(filename, 'w') as file: # Open the same file for writing and overwrite its contents
            for line in lines:
                words = line.split()  # Split the line into words
                new_line = []  # To store words without numbers

                line_sum = 0.0  # Initialize the line sum to 0.0

                for word in words:
                    try:
                        num = float(word)  # Try to convert the word to a float
                        line_sum += num  # Add the number to the line sum
                    except ValueError:
                        new_line.append(word)  # If not a number, add it to the new_line list

                # Write the modified line to the file
                file.write(' '.join(new_line) + '\n')
                print(line_sum)
    # File Not Found exception handling
    except FileNotFoundError:
        print(f"ERROR: {filename} not found.")
        sys.exit(1)