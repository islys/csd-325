# Ryan Monnier
# CSD 325
# Module 8 assignmnet
# 19-Feb-2025


# import json, and I was having trouble getting it to see the .json file, even though its in the same dir as the script, so I imported os
import json
import os

# sets cwd to ../module-8 so my script can find the .json
os.chdir('C:/csd/csd-325/module-8')

# set var for future use
students = {}
me = {}


# open up the .json and put the data into a list
with open('student.json', 'r') as file:
    students = json.load(file)


# function to create a dictionary of the .json contents
def print_student_list(students):
    for student in students:
        print(f"{student['F_Name']} {student['L_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

# printing unaltered list
print("Original Student List:")
print_student_list(students)

# adding myself as a dictionary
me = {
    "F_Name": "Ryan",
    "L_Name": "Monnier",
    "Student_ID": 12345,
    "Email": "ryan.monnier@bellevue.edu"
}

students.append(me)

# printing the new student list
print("\nNew and improved student list:")
print_student_list(students)

# writing our changes back to the .json file
with open('student.json', 'w') as file:
    json.dump(students, file, indent=4)

# required notification that changes have been made
print("\nThe student.json file has been updated.")