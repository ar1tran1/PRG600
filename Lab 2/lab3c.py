'''
Name: Aritra Nandy
Student ID : 137916227
description  : Lab3c
'''


sum = 0 #initalize sum value zero

print("SUMMING CALCULATOR") 
while True: 
    print("The sum so far: " + str(sum)) #show sum output as string
    user_input = input("Enter a number to add to your sum. Pressing Enter will exit. ") #take user input of sum value 
    if user_input == "": #check if user value is equal to entered value
        break 
    else:  
        sum = sum + int(user_input)
print("Thank you for using summing calculator. The final sum was " + str(sum) + ".")#output of sum as string value