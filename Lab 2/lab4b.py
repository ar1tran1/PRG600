from random import randint

def rtrn_area(length, width): # function which takes length and width  as parameters and returns area 
 "Takes length and width as parameters and returns the area"
 return length * width

rect = rtrn_area(5, 3)
# call the function again with new values
def rtrn_area(length, width):
 return length * width
rect = rtrn_area(4,6)

def print_all_caps(name, age): # takes name and age as parameters
 "A function which takes name and age as parameters and prints the name and age"
cap_name = name.upper()
print('THIS PERSON\'S NAME IS ' + cap_name + ' AND THEY ARE ' + str(age)
+ ' YEARS OLD!!!')

print_all_caps('eric', 41)
print_all_caps('melissa', 40)
# call the function again with new values

def print_all_caps(name, age): # takes name and age as parameters
 cap_name = name.upper()
print('THIS PERSON\'S NAME IS ' + cap_name + ' AND THEY ARE ' + str(age)
+ ' YEARS OLD!!!')
print_all_caps('lisa',35)

def get_rando(): # picks a random number between a certain range
 "this function picks a random number between 1 and 101 and retruns that number"
 return randint(1, 101)

lucky_num = get_rando()
# call the function again with new values
def get_rando():
 return randint(70, 100)
lucky_num = get_rando()

def is_odd(num): # takes integer as parameters from user
 "takes input and checks if it is a odd number"
 if num % 2 == 1:
   return True
 else: 
   return False

print(is_odd(13))
print(is_odd(get_rando()))
# call the function again with new values
def is_odd(num): # takes integer as parameters from user
 if num % 2 == 1:
   return True
 else: 
   return False
print(is_odd(23))
print(is_odd(get_rando()))

if __name__ == "__main__":
 print(is_odd(13))
