# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 19:31:36 2020

@author: bhara_5sejtsc
"""

a = float(input("Enter one number: "))
b = float(input("Enter another number: "))

print("select operation:")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter a choice 1/2/3/4: ")

if (choice == '1'):
	print(a, "+", b, "=", a+b)
	
elif (choice == '2'):
	print(a, "-", b, "=", a-b)

elif (choice == '3'):
	print(a, "*", b, "=", a*b)
	
else:
	print(a, "/", b, "=", a/b)