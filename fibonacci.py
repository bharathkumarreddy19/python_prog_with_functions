# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 19:55:58 2020

@author: bhara_5sejtsc
"""

def fibonacci(n):
	if n<=1:
		return n
	else:
		return (fibonacci(n-1)+fibonacci(n-2))
	
nterms = int(input("Enter how many terms do you want: "))

if nterms <= 0:
	print("Please enter a positive integer")
else:
	for i in range(nterms):
		print(fibonacci(i))
		
	
