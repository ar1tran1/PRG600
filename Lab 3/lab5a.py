'''
Name: Aritra Nandy

Student ID: 137916227



 '''

def my_sum(int_list): #defining mysum function
  total_sum = 0
  for number in int_list:
    total_sum += int(number)
  return total_sum

if __name__ == "__main__":
    my_list = [] 
    print("AVERAGE CALCULATOR")
    while True:
        user_input = input("Enter a number to add to your sum. Pressing Enter will exit. ")
        if user_input == "":
            break
        else: 
            my_list.append(int(user_input))
    num_sum = my_sum(my_list)
    num_length = len(my_list)
    average = num_sum / num_length
    print(f"Total sum is: {num_sum}. Total count is: {num_length}. Average for this list is: {average}.")
    print("Thank you for using the average calculator.")
