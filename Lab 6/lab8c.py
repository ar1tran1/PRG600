'''
Aritra Nandy
137916227
Lab8c
'''

import os

def check_internet_connectivity():
    print("Checking internet connectivity...")
    exit_code = os.system("ping -c 4 google.com")  # Linux/Mac
    if exit_code == 0:
        print("The Internet is UP.")
    else:
        print("Internet connectivity issue detected.")

def greet_user():
    username = os.popen("whoami").read().strip()
    print(f"Welcome, {username}.")

def print_system_info():
    print("Printing system information...")
    if os.name == "posix":  # Check if the OS is Linux/Mac
        os.system("uptime")
    elif os.name == "nt":  # Check if the OS is Windows
        os.system("systeminfo")
    else:
        print("Unsupported operating system.")

if __name__ == "__main__":
    
    check_internet_connectivity() # Check internet connectivity

    
    greet_user() # Greet the user

    
    print_system_info() # Print system information
