# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 18:50:58 2020

@author: bhara_5sejtsc
"""
import sys

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def lcm(a,b):
	large = max(a,b)
	small = min(a,b)
	i = large
	while(1):
		if (i%small == 0):
			return i
		i += large
		
		
print("LCM of a,b=",lcm(a,b),sep='')
			
	