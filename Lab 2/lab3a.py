'''
Name : Aritra Nandy
Student ID : 137916227
Description: Lab3a

'''
point = 0
num = 0
while num != 26: 
    user_input = input("Enter the answer to 12 + 14, or press 's' to skip: ") 
    if user_input == 's':
        print("Question skipped. 0 points awarded") 
        break 
    else: 
        num = int(user_input) 
    if num != 26: 
        print("Incorrect. Try again.") 
    else: 
        print("Correct! You have been awarded 1 point!") 
        point=point+1
print("Next question...")

while num!=31:
    user_input= input("Enter the answer to 23 + 8 or press 's' to skip:")
    if user_input=='s':
        print("Question skipped. 0 points awarded")
        break
    else:
        num=int(user_input)
        if num!=31:
            print("Incorrect. Try again.")
        else:
            print("Correct! You have been awarded 1 point")
            point=point+1
print("Next question...")

while num!=43:
    user_input= input("Enter the answer to 30+13 or press 's' to skip:")
    if user_input=='s':
        print("Question skipped. 0 points awarded")
        break
    else:
        num=int(user_input)
        if num!=43:
            print("Incorrect. Try again.")
        else:
            print("Correct! You have been awarded 1 point")
            point=point+1
print("Next question...")

while num!=44:
    user_input= input("Enter the answer to 17+27 or press 's' to skip:")
    if user_input=='s':
        print("Question skipped. 0 points awarded")
        break
    else:
        num=int(user_input)
        if num!=44:
            print("Incorrect. Try again.")
        else:
            print("Correct! You have been awarded 1 point")
            point=point+1
final_result = ((point/4) * 100)
print(f"You received a grade of {final_result:.1f}%.")
