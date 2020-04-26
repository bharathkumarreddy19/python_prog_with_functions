# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 20:13:40 2020

@author: bhara_5sejtsc
"""

def factorial(n):
	return 1 if (n == 0 or n== 1) else n*factorial(n-1)

n = int(input("Enter a number to find factorial: "))

print("Factorial of n is",factorial(n))	
