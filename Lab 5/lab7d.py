'''
Name : Aritra Nandy
ID : 137916227
Description : Lab7d
'''
import csv 
import sys

# This function, dict_reader, reads data from a CSV file specified by the 'filename' parameter.
# It opens the file, uses csv.DictReader to read the contents into a list of dictionaries,
# and then closes the file before returning the list_of_dicts.


def dict_reader(filename):
    list_of_dicts = [] 
    f = open(filename, 'r') 
    reader = csv.DictReader(f) 
    for row in reader: 
        list_of_dicts.append(row) 
    f.close()
    return list_of_dicts

# This function, dict_writer, writes a list of dictionaries to a CSV file specified by the 'filename' parameter.
# It opens the file in write mode, obtains the field names from the first dictionary in the list_of_dicts,
# uses csv.DictWriter to write the header with the field names, iterates through the list_of_dicts to write
# the data rows, and finally, closes the file.



def dict_writer(filename, list_of_dicts):
    f = open(filename, 'w') 
    fieldnames = list_of_dicts[0].keys() 
    w = csv.DictWriter(f, fieldnames=fieldnames) 
    w.writeheader() 
    for row in list_of_dicts: 
        w.writerow(row) 
    f.close()

if __name__=="__main__":
    if  len(sys.argv)==1: #if user only type the name of the script , prints a usage message
        print("Usage: lab7d.py filename")
    elif len(sys.argv) == 2:
        try:
            list_of_dict = dict_reader(sys.argv[1])
            for dict in list_of_dict:
                if dict['First Name'] == 'Christoper':
                    dict['First Name'] = 'Chris'
                if dict['Last Name'] == 'Patal':
                    dict['Last Name'] = 'Patel'
                if dict['Last Name'] == 'Smith':
                    dict['Last Name'] = 'Nichols'
                if dict['Address'] == '81 Vanier':
                    dict['Address'] = '72 Princeton'
                if dict['Last Name'] == 'Geary':
                    dict['Address'] = '455 Bloor'
                if dict['City'] == 'North York':
                    dict['City'] = 'Toronto'
                if 'Country' in dict and dict['Country'] == 'Canada':
                    dict['Country'] = 'CA'                  
            dict_writer(sys.argv[1], list_of_dict)
        except FileNotFoundError:
            print("File not found")
            sys.exit(1)