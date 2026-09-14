"""Python Basics Exercise

Complete each question by writing Python code below its comments.
Run the file after each question to test your work.
"""

# %%
# Question 1: 
# Create two variables named student_name and Student_Name.
# Give them different string values, then print both variables on separate lines.
# Add a single-line comment explaining why Python treats these as
# two different variables.

student_name = "James"
Student_Name = "John"
# these are different variables because the latter of the two is capitalized, and Python is case sensitive


# %%
# Question 2: Strings and quotation marks
# Create one string using double quotes and another using single quotes.
# Print both strings. Did it work either way or was there an error?

print("This is a string with double quotes.")
print('This is a string with single quotes.')
# Output worked for both strings, no errors occurred.

print('Hello "this is an example with quotes"')

# %%
# Question 3: 
# Use ONE print() statement and escape sequences to display this output:
# Python Basics
#     Strings are fun!
# "Practice makes progress."

print("\tPython Basics\n\tStrings are fun!\n\t\"Practice makes progress.\"")

# %%
# Question 4: 
# Store "10" and "5" in two variables as strings. Add them and print the
# result. Then store 10 and 5 in two variables as numbers, add them, and
# print the result. Add a comment explaining why the results are different.

num1 = "10"
num2 = "5"
result = num1 + num2
print(result)

num1 = 10
num2 = 5
result = num1 + num2
print(result)


# %%
# Question 5: 
# Create variables for a person's name (string) and age (integer).
# Use the + operator to display a sentence such as "Ava is 20 years old."
# If you had any errors describe what the issue was in a short comment

name = "Ava"
age = 20
print(name + " is " + str(age) + " yrs old.")
# or
print(f"{name} is {age} yrs old.")

#originally my spacing was off, I had to add a space on either side of the "is" within the quotations

# %%
# Question 6: 
# Create a constant named COURSE_NAME and assign it "Introduction to Python".
# Create variables for a student's name and current grade.
# Use an f-string to print a sentence containing the student name, grade,
# and course name. Example: "Sam has 85% in Introduction to Python."

COURSE_NAME = "Introduction to Python"

stu_name = "James"
curr_grade = float(85.6)

print(f"{stu_name} has {curr_grade} in {COURSE_NAME}")


# %%
# Question 7:
# True or False? By naming our constant in question 6 in all caps it prevented us
# from changing the value of that constant later in our code.

## FALSE Its a style to tell other programmers not to change it - pyhton does not "lock it"

# %%
# Question 8: Student Introduction
#
# Ask the user to enter:
# - Their name
# - Their program name
# - Their favourite programming language
#
# Store each answer in a properly named variable
#
# Use an f-string and escape sequences to display the information
# on separate lines, similar to this:
#
# Student Information
#     Name: Sam
#     Program: Digital Media and IT
#     Favourite language: Python


user_name = input("Please input user name: ")
user_prog = input("Please input user program: ")
fav_lang = input("Please input favorite language: ")

print(f" Name: {user_name} \n Program: {user_prog} \n Favorite Language: {fav_lang}")



# %%
# Challenge Question!
# Create an Interactive Student Course Summary
#
# Ask the user to enter:
# - Their name
# - Their first score
# - Their bonus score
#
# Example input:
# Student name: Sam O'Neil
# First score: 85
# Bonus score: 10
#
# After receiving the input, produce this output:
#
# *** Python Results ***
# Student: Sam O'Neil
# Course: "Introduction to Python"
# Scores as strings: 85 + 10 = 8510
# Scores as numbers: 85 + 10 = 95
# Sam O'Neil's final grade in "Introduction to Python" is 95%.
#
# Requirements:
#
# 1. Create a constant named COURSE_NAME containing:
#    Introduction to Python
#
# 2. Use input() to ask the user for their name.
#    Store the input in a properly named variable.
#
# 3. Use input() to ask the user for their first score and bonus score.
#    Store both answers as strings.
#
# 5. Add the two score strings together and store the result.
#    Add a comment explaining why "85" + "10" produces "8510".
#
# 6. Convert both score strings to integers using int().
#    Add the numbers to calculate the student's final grade.
#
# 7. Use ONE print() statement to display:
#    - The heading
#    - The student's name
#    - The course name in quotation marks
#    - The result of adding the scores as strings
#    - The result of adding the scores as numbers
#
#    This print() statement must use:
#    - String concatenation with the + operator
#    - Escape sequences such as \n, \t, \' or \"
#    - str() when concatenating a number
#
# 8. Use a separate print() statement and an f-string to display:
#
#    Sam O'Neil's final grade in "Introduction to Python" is 95%.
#
# 9. Use both single and double quotation marks appropriately.
#
#

COURSE_NAME = "\"Introduction to Python\""

name = input("Please insert student name: ")
first_score = input("Please insert first score: ")
bonus_score = input("Please insert bonus score: ")

str_scores = (first_score + bonus_score)
# This just combines 2 strings together
# they have to be converted to a int before a operation is possible

num1 = int(first_score)
num2 = int(bonus_score)

final_score = (num1 + num2)

print(f"\t*** Python Results ***\n\tStudents Name: {name}\n\tCourse: {COURSE_NAME}\n\tScores as strings: {str_scores}\n\tScores added together: {final_score}")




# %%
# create a variable and store your phone number in it
 
james_ph = "780-108-1002"
print(james_ph)

# %%
