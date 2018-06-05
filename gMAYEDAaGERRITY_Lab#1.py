
###################################################################################################################
#    Programmers: Grace Mayeda, Andrew Gerrity
#    Course: CS201.03, Professor Stefanelli
#    Assignment Due Date: 9/13/2015
#    Lab Assignment: 1
#    Problem Statement: Create a program that will, based on a given number of mL provided by the user, output the
#                       equivalent numbers of teaspoons, the equivalent number of tablespoons, and the equivalent
#                       number of cups, for the same number of mL, to help the user using your program to cook from
#                       recipes based on metric measures.
#    Data In: User name and mL quantity
#    Data Out: User's given name and converted teaspoon, tablespoon, and cup quantities from mL
#    Algorith: See attached paper for algorithm
#    Other (non-standard) classes needed for code to compile: None
#    Credits: Based on the code provided in class and course text
####################################################################################################################



print("This program will convert mL to teaspoons, tablespoons, and cups.")

import math

#User = input ("Enter name: ")
mL_str = input ("Enter amount of mL to be converted: ")
mL_int = int(mL_str)

teaspoon = 0.2 * mL_int #There are 5 mL in each teaspoon
tablespoon = 0.0666667 * mL_int #There are 3 teaspoons in each tablespoon
cup = 0.004167 * mL_int #There are 16 tablespoons in each cup

print("teaspoons:" ,teaspoon)
print("tablespoons:" ,tablespoon)
print("cups: " ,cup)
