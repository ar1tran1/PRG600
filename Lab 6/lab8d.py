'''
Aritra Nandy
137916227
Lab8d
'''

import os

course_dir = '.'  # Change this to the target directory


print('Your current directory is:', os.path.abspath(course_dir)) # Display the current directory


for root, directories, filenames in os.walk(course_dir): # Recursive listing of directory contents using os.walk
    for directory in directories:
        print(os.path.join(root, directory))

    for filename in filenames:
        print(os.path.join(root, filename))
