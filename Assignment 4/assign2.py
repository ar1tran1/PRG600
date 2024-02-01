'''
Name: Aritra Nandy
Myseneca: anandy
ID: 137916227
Description: Store Stock tracker assignment 4
'''
import csv
import sys


def dict_reader(filename): # Function to read a CSV file and return a list of dictionaries
    list_of_dicts = []
    
    with open(filename, 'r') as f: # Use a 'with' statement to ensure proper file handling
        reader = csv.DictReader(f)
        for row in reader:
            list_of_dicts.append(row)
    return list_of_dicts


def list_printer(data_list): # Function to print a list of dictionaries or lists in a tabular format
    if not data_list:
        return

    if isinstance(data_list[0], dict):
        # List of dictionaries
        header_printed = False
        count = 1

        for dicts in data_list:
            if not header_printed:
                print("#", end=' ')
                for key in dicts:
                    print(f"{key : ^20} ", end=' ')
                print("\n" + '=' * (20 * len(dicts) + 2))
                header_printed = True

            print(f"{count}", end=' ')
            count += 1
            for key, value in dicts.items():
                print(f"{value : ^20} ", end=' ')
            print()

    elif isinstance(data_list[0], list):
        # List of lists
        header_printed = False
        count = 1

        for data_row in data_list[1:]:
            if not header_printed:
                #print("#", end=' ')
                for header in data_list[0]:
                    print(f"{header : ^20} ", end=' ')
                print("\n" + '=' * (20 * len(data_list[0]) + 2))
                header_printed = True

            #print(f"{count}", end=' ')
            count += 1
            for value in data_row:
                print(f"{value : ^20} ", end=' ')
            print()



def generate_reports(data, lost_sales): # Function to calculate total sales, lost sales, and restock report
    total_sales_report = []
    lost_sales_report = []
    restock_report = []

    total_sales_header = ['#', 'Item', 'Sales', 'Price per Item', 'Total']
    lost_sales_header = ['#', 'Item', 'Sales', 'Price per Item', 'Total']
    restock_header = ['#', 'Item', 'Demand', '20% Demand', 'Total Demand', 'Current Stock', 'From Warehouse']

    total_sales_report.append(total_sales_header)
    lost_sales_report.append(lost_sales_header)
    restock_report.append(restock_header)

    grand_total = 0

    for item in data:
        item_name = item['Item']
        sales = int(item.get('Sales', 0))
        price_per_item = float(item.get('Price per Item', 0))
        current_stock = int(item.get('Current Stock', 0))
        demand = sales + lost_sales.get(item_name, 0)
        twenty_percent_demand = round(demand * 0.2)
        total_demand = demand + twenty_percent_demand

        
        total_sales = sales * price_per_item # Calculate total sales and grand total
        grand_total += total_sales

        # Generate total sales report
        total_sales_report.append([data.index(item) + 1, item_name, sales, f"${price_per_item:.2f}", f"${total_sales:.2f}"])

        # Generate lost sales report
        if lost_sales.get(item_name, 0) > 0:
            lost_sales_report.append([data.index(item) + 1, item_name, lost_sales[item_name],
                                      f"${price_per_item:.2f}", f"${lost_sales[item_name] * price_per_item:.2f}"])

        # Generate restock report
        from_warehouse = max(twenty_percent_demand, total_demand - current_stock)
        current_stock = max(0, current_stock - from_warehouse)
        restock_report.append([data.index(item) + 1, item_name, demand, twenty_percent_demand, total_demand,
                            current_stock, from_warehouse])




    
    total_sales_report.append(['TOTAL', '', '', '', f"${grand_total:.2f}"]) # Generate total sales report

    return total_sales_report, lost_sales_report, restock_report

# Function to write reports to CSV
def export_reports(total_sales_report, lost_sales_report, restock_report, output_filename):
    with open(output_filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(total_sales_report)
        writer.writerows([''])  # Add an empty line between reports
        writer.writerows(lost_sales_report)
        writer.writerows([''])
        writer.writerows(restock_report)

if __name__ == "__main__":
    # Check for the correct number of command line arguments
    if len(sys.argv) != 3:
        print("Usage: assign2.py input_filename output_filename")
        sys.exit(1)

    
    input_filename = sys.argv[1] # Read the CSV file into a list of dictionaries
    data = dict_reader(input_filename)

    # Initialize lost sales dictionary
    lost_sales = {}

    while True:
        # Print the modified data in a tabular format
        list_printer(data)

        selection = input(f"Select a number (1-{len(data)}) to indicate a sale, or 'e' to indicate end of day:")
        try:
            if selection.lower() == 'e':
                break
            else:
                selection = int(selection) - 1
                if 0 <= selection < len(data):
                    item_name = data[selection]['Item']
                    current_stock = int(data[selection]['Current Stock'])
                    if current_stock > 0:
                        data[selection]['Current Stock'] = str(current_stock - 1)
                        if 'Sales' in data[selection]:
                            data[selection]['Sales'] = str(int(data[selection]['Sales']) + 1)
                        else:
                            data[selection]['Sales'] = '1'
                    else:
                        print(f"Stock for {item_name} is already 0. Cannot sell more.")
                        if item_name in lost_sales:
                            lost_sales[item_name] += 1
                        else:
                            lost_sales[item_name] = 1
                else:
                    print("Invalid selection")
        except ValueError:
            print("Invalid input. Please enter a number or 'e'.")

    # Generate reports
    total_sales_report, lost_sales_report, restock_report = generate_reports(data, lost_sales)

    # Display reports using list_printer instead of dict_printer
    print("\nTotal Sales Report:")
    list_printer(total_sales_report)

    print("\nLost Sales Report:")
    list_printer(lost_sales_report)

    print("\nRestock Report:")
    list_printer(restock_report)

    # Export reports to CSV
    export_reports(total_sales_report, lost_sales_report, restock_report, sys.argv[2])