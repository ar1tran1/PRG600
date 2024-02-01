'''''
Name: Aritra Nandy
Myseneca : anandy
Group 4
Description: Shopping Calcutlator
'''
def get_item_price(): #Get item price function to validate input
    while True:
        item_price = input("Please enter the price for this item: ")
        try:
            item_price = float(item_price)
            break
        except:
                print("Error: price must be a number. Example: 1, or 1.99.")
    return item_price

def get_item_quantity():# Get quantity function to validate input
    while True:
        item_quantity = input("Please enter the quantity for this item: ")
        try:
            item_quantity = int(item_quantity)
            break
        except:
            print("Error: price must be a number.")
    return item_quantity

# Function to apply discounts to item prices
def apply_discount(item_name, quantity, price): #apply_discount function takes 3 parameters and returns either dicounted price or price
    # List of items eligible for a discount
    discount_items = ['candy', 'eggs', 'flour', 'hummus', 'ice cream', 'chicken soup', 'diapers']

    if item_name.lower() in discount_items: # if item is in discount list
        # Calculate the discount
        discount = min(20, (quantity - 1) * 5) # Use of min function to guarantee that discount % is capped at 20%
        # Apply the discount to the price
        discounted_price = price - (price * discount / 100)
        return discounted_price
    else:
        return price

# Initialize variables for the receipt and total discount
receipt = []
total_discount = 0
total_cost = 0.0
print("Shopping Calculator")
while True:
    item_name = input("Please enter an item of food, or press Enter to exit: ")
    
    if item_name == '':
        break

    price = get_item_price() # Call get_item_price function and save in variable

    quantity = get_item_quantity() # Call get_item_quantity and save in variable

    # Apply discounts and calculate the item cost
    item_cost = apply_discount(item_name, quantity, price) 

    # Add the item to the receipt
    receipt.append(f"{item_name:<10} {quantity} x $ {item_cost:.2f} = $ {quantity * item_cost:.2f}")

    # Update the total discount
    if item_cost < price:
        total_discount += (price - item_cost) * quantity
    
    # Update the total cost
    total_cost += quantity * item_cost
# Print the receipt
print("\nRECEIPT")
for i, item in enumerate(receipt, 1):
    print(f"{i}. {item}")

print(f"Total:                    $ {total_cost:.2f}")
print(f"You saved:                 $ {total_discount:.2f}")
