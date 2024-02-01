'''
Name : Aritra Nandy
ID : 137916227
Description : Lab7c
'''
# Import the print_meal_plan function from the lab7b
from lab7b import print_meal_plan
import sys

# Template for a day's meal plan
template = {'breakfast': None, 'lunch': None, 'dinner': None}

if __name__ == "__main__":
    # List to store meal plans for each day
    days = []

    while True:
        # Create a new day based on the template
        new_day = template.copy()

        # Ask the user if they want to add a day
        answer = input("Would you like to add a day? (y/n) ")

        # Check the user's response
        if answer.lower() == 'y':
            # Ask the user for meal choice for each time
            for key in new_day:
                new_day[key] = input(f"Please enter what you would like to eat for {key}:")
            
            # Append the new day's meal plan to the list of days
            days.append(new_day)
        elif answer.lower() == 'n':
            # Break out of the loop if the user chooses not to add another day
            break
        else:
            # Deal with invalid input
            print("Invalid answer. Please enter 'y' or 'n'")

    # Check if any days were added
    if len(days) == 0:
        print("Exiting...")
        sys.exit(0)

    try:
        # Ask the user for a day number to print the menu
        day = int(input(f"Please enter a day number for the menu you would like to print (1-{len(days)}):"))
        
        # Print the meal plan for the selected day
        print_meal_plan(days[day - 1])
    except IndexError:
        # Handle an invalid day number
        print("Invalid day number. No menu for the selected day.")
        sys.exit(1)
    except ValueError:
        # Handle invalid input for day number
        print("Invalid input. Please enter a valid day number.")
        sys.exit(1)
