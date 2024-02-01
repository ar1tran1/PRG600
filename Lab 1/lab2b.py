#Aritra Nandy
#137916227

#Get the gross income from the user
user_income = input("Please enter your gross income ")
#Get the number of dependants from the user
user_dep = input("Please enter your number of dependents ")
#Convert the income to float datatype
income = float(user_income)
#Convert the depandant to integer datatype
dependants = int(user_dep)
if income <=32000: #Check if the income is lower or equal to 32000
    tax_rate = 0.1 #Tax rate should be 10% for the above condition
elif 32000<income<=64000: #Check if income is between 32000 and 64000
    tax_rate = 0.15 #Tax rate should be 15% for the above condition
else:
    tax_rate = 0.25 #For all other conditions tax rate should be 25%
taxable_income=int(income- 10000-(dependants*2000)) #Deduct the amount from gross income
income_tax = int(taxable_income * tax_rate) #Apply the tax rate accordingly
if income_tax<0: #Output is 0 if income tax lower than 0
    income_tax = 0
tax=str(income_tax) #Convert the income_tax to a string datatype
print("The income tax is $"+ tax)