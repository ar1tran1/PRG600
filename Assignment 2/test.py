# Initialize the list of discounted items and their discount rate
discounted_items = ['candy', 'eggs', 'flour', 'hummus', 'ice cream', 'chicken soup', 'diapers']
discount_rate = 0.05  # 5% discount per additional item, up to a maximum of 20%

# Initialize the variables to keep track of the total cost and the total discount
total_cost = 0.0
total_discount = 0.0

# Create an empty dictionary to store the item information
items = {}

# Function to calculate the discounted price of an item
def calculate_discounted_price(item_price, item_count):
    max_discount = 0.20  # 20% maximum discount
    total_discount = 0.0

    if item_name.lower() in discounted_items:
        # Calculate the discount
        eligible_items = min(item_count, 5)  # Up to 5 items can be discounted
        discount_amount = eligible_items * item_price * discount_rate
        total_discount += discount_amount

        # Apply the discount to the item price
        discounted_price = item_price - (discount_amount / item_count)
        return discounted_price, total_discount
    else:
        return item_price, total_discount

# Print the shopping calculator title
print("Shopping Calculator")

# Input loop to get item information from the user
while True:
    item_name = input("Please enter an item of food, or press Enter to exit: ")
    
    if item_name == "":
        break  # Exit the loop if the user presses Enter
    
    item_price_input = input(f"Item is: {item_name}. Please enter the price for this item: ")
    
    try:
        item_price = float(item_price_input)  # Convert the input to a float
        item_count = int(input(f"Item is: {item_name}. How many will you purchase: "))
        
        item_price, item_discount = calculate_discounted_price(item_price, item_count)
        
        # Update total cost and total discount
        total_cost += item_price * item_count
        total_discount += item_discount
        
        # Add the item to the dictionary
        items[item_name] = (item_count, item_price)
        
    except ValueError:
        print("Error: price must be a number. Example: 1, or 1.99.")

# Print the receipt
print("RECEIPT")
for i, (item, (count, price)) in enumerate(items.items(), start=1):
    item_total = count * price
    print(f"{i}. {item} {count} x $ {price : .2f} = $ {item_total : .2f}")

print(f"Total: $ {total_cost : .2f}")
print(f"You saved: $ {total_discount : .2f}")