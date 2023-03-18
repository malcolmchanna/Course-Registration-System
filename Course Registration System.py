#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


# Course registration system

# Define a list of departments and their courses
departments = {
    "Computer Science": ["CS101", "CS102", "CS201", "CS202"],
    "Mathematics": ["MATH101", "MATH102", "MATH201", "MATH202"],
    "Physics": ["PHYS101", "PHYS102", "PHYS201", "PHYS202"]
}

# Define a list of semesters
semesters = ["Fall", "Spring", "Summer"]

# Define a list of users
users = []

# Define a function for user sign up
def sign_up():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    user = {"name": name, "email": email, "password": password}
    users.append(user)
    print("User signed up successfully.")

# Define a function for user login
def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    for user in users:
        if user["email"] == email and user["password"] == password:
            print("User logged in successfully.")
            return
    print("Invalid email or password.")

# Define a function for course registration
def register_course():
    department = input("Enter the department: ")
    if department not in departments:
        print("Invalid department.")
        return
    semester = input("Enter the semester: ")
    if semester not in semesters:
        print("Invalid semester.")
        return
    courses = departments[department]
    print("Available courses:")
    for course in courses:
        print(course)
    course_code = input("Enter the course code: ")
    if course_code not in courses:
        print("Invalid course code.")
        return
    print("Course registered successfully.")

# Main program loop
while True:
    print("1. Sign up")
    print("2. Login")
    print("3. Register course")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        sign_up()
    elif choice == "2":
        login()
    elif choice == "3":
        register_course()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")

        


# In[ ]:




