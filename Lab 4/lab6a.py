'''
Name: Aritra Nandy
ID : 137916227/anandy
Description : Lab6a
'''
data_to_write = ['First Line!', 'Second Line!!', 'Third Line!!!', '...and so on!']

# Open a file in the current directory with write ('w') mode
with open('testing.txt', 'w') as file:
    # Write each element from the data_to_write list into the file
    for line in data_to_write:
        file.write(line + '\n')  # Add a newline character to separate lines
