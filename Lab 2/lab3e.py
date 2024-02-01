'''
Name : Aritra Nandy
Student id : 137916227
description : Lab3e
'''
from random import randint

random_num1 = randint(1,10)
random_num2 = randint(1,10)
sum = random_num1 + random_num2
qa = 0
point = 0
user_input = 0
while user_input !=sum:
    user_input = input(f"Enter the answer to {random_num1} + {random_num2} , or press 's' to skip or 'q' to quit") #taking use input
    if user_input=='q': #break if user input is q
     break
    elif user_input == 's': #break the loop if user input is s
       print("Skip the question")
       random_num1 = randint(1,10)
       random_num2 = randint(1,10)
       sum=random_num1 + random_num2
       qa +=1
    elif int(user_input) !=sum: #convert the user input to int for num variable
       print("Incorrect, Try again")
    else:
       random_num1 = randint(1,10)
       random_num2 = randint(1,10)
       sum = random_num1 + random_num2
       print("Correct! You have been awarded 1 point!") 
       qa+=1
       point+=1 #increase point count by 1 if correct

final_result = ((point/qa)*100)
print(f"Quiz Over. You scored {final_result:.1f}%.")