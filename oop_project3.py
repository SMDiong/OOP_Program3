# Diong, Shan Marc C.
# March 23, 2024
# Project 3

# Word Formatting for Fancy Words
from art import *
green = "\033[0;32m"
blue = "\033[0;34m"
color_reset = "\033[0m"

# This will ask the user what's their name
user_name = input(green + "Please enter your name: ")

# This will ask the user what's their age
user_age = input("Please enter your age: ")

# This will ask the user what's their sex
user_sex = input("Please enter your sex: ")

# This will ask the user what's their dream job
dream_job = input("Please enter your dream job: ")

# This will ask the user what's their email address
email_address = input("Please enter your email address: ")

# This will ask the user what's their current city
user_city = input("Please enter your city: ")

# This will ask the user what's their school
user_school = input("Please enter your school: ")

# This will ask the user what's their course
user_course = input("Please enter your course: " + color_reset)

# Print name input in a fancy way
print("\n")
print(blue + text2art(user_name, font="block",))

# Print age input in a fancy way
print("\n")
print(text2art(user_age, font="block"))

# Print sex input in a fancy way
print("\n")
print(text2art(user_sex, font="block"))

# Print dream job input in a fancy way
print("\n")
print(text2art(dream_job, font="block"))

# Print email address input in a fancy way
print("\n")
print(text2art(email_address))

# Print city input in a fancy way
print("\n")
print(text2art(user_city, font="block"))

# Print school input in a fancy way
print("\n")
print(text2art(user_school, font="block"))

# Print course input in a fancy way
print("\n")
print(text2art(user_course, font="block"))

#end