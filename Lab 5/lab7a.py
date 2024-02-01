'''
Name : Aritra Nandy
ID : 137916227
Description : Lab7a
'''

def shipping_label(a_lst): 
    "takes a list, generates a string"
    a_str = f"{a_lst['first_name'].capitalize()} {a_lst['last_name'].capitalize()}\n"
    a_str += f"{a_lst['addr1']}\n"
    a_str += f"{a_lst['city']}, {a_lst['prov']}\n"
    a_str += f"{a_lst['pcode']}"
    return a_str

student1 = {'first_name': 'eric', 'last_name':'smith', 'addr1': '217 Au Large Blvd', 'city': 'Toronto', 'prov': 'Ontario', 'pcode': 'M4A 1P3'}

# Call the function with student1 as an argument and print the result
label = shipping_label(student1)
print(label)
