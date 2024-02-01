'''
Aritra Nandy
137916227
Lab8b
'''

import re
import sys

def validate_variable_name(name):
    
    variable_name_regex = r'^[a-z][a-z0-9_]{2,15}$' # Regex to match Python variable names
    return re.match(variable_name_regex, name) is not None

def match_phone_numbers_in_file(filename):
    
    phone_number_regex = r'\d{3}-\d{3}-\d{4}' # Regex to match phone numbers

    
    with open(filename, 'r') as file: # Read the contents of the file
        file_contents = file.read()

    
    phone_numbers = re.findall(phone_number_regex, file_contents) # Use findall to match all phone numbers

    
    print(f'Number of phone numbers found: {len(phone_numbers)}') # Print the number of results found

    
    user_input = input('Do you want to see the results? (y/n): ') # Ask the user if they want to see the results

    if user_input.lower() == 'y' or user_input == '':
        
        for i, phone_number in enumerate(phone_numbers, start=1): # Print each phone number found
            print(f'{i}. {phone_number}')

if __name__ == "__main__":
    
    if len(sys.argv) != 2: # Check if a filename is provided as a command line argument
        print('Usage: python lab8b.py <filename>')
        sys.exit(1)

    filename = sys.argv[1]

    
    match_phone_numbers_in_file(filename) # Call the function to match phone numbers in the file
