# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 19:14:43 2020

@author: bhara_5sejtsc
"""
import sys

def hcf(a,b):
	if(b == 0):
		return a
	return hcf(b,a%b)
	
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
	
print("HCF of a,b is",hcf(a,b),sep='')