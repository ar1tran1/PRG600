'''
Aritra Nandy
137916227
Lab8e
'''

import os
import shutil
import sys

def backup_script(target_directory):
    
    if not os.path.isdir(target_directory): # Check if the target directory is valid
        print(f"Error: {target_directory} is not a valid directory.")
        sys.exit(1)

    
    backup_directory = os.path.join(target_directory, 'backups') # Define the backup directory

    
    if not os.path.exists(backup_directory): # Check if the backup directory exists, if not, create it
        os.makedirs(backup_directory)

    
    for root, directories, filenames in os.walk(target_directory): # Walk through the target directory
        for filename in filenames:
            file_path = os.path.join(root, filename)

            
            if filename.endswith('.py'): # Check if the file is a Python script

                
                if not os.path.commonpath([file_path, backup_directory]) == backup_directory: # Check if the file is not inside the backup directory

                    
                    shutil.copy(file_path, os.path.join(backup_directory, filename)) # Create a copy in the backups directory
                    print(f"Copied {filename} to backups directory.")

if __name__ == "__main__":
    
    if len(sys.argv) != 2: # Check if the command line argument is provided
        print("Usage: python lab8e.py <target_directory>")
        sys.exit(1)

    target_directory = sys.argv[1]
    backup_script(target_directory)
