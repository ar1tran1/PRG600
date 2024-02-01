'''
Name : Aritra Nandy
ID : 137916227
Description : Lab7b
'''
# Define a meal plan dictionary
meal_plan = {'breakfast': 'oatmeal', 'lunch': 'sandwiches', 'dinner': 'broccoli'}

# Function to print the meal plan
def print_meal_plan(a_dict):
    # Set the width for formatting
    width = 50

    # Print the header for the meal plan
    print(f"{'MENU FOR TODAY' : ^{width}}")
    print('=' * width)

    # Print each meal
    print(f"{'Breakfast' : <25}{a_dict['breakfast'] : >25}")
    print(f"{'Lunch' : <25}{a_dict['lunch'] : >25}")
    print(f"{'Dinner' : <25}{a_dict['dinner'] : >25}")

    return

# Check if the script is run directly
if __name__ == "__main__": 
    # Call the function to print the meal plan
    print_meal_plan(meal_plan)
