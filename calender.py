# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 19:43:08 2020

@author: bhara_5sejtsc
"""

import calendar

yy = int(input("Enter a year: "))
mm = int(input("Enter a month: "))


print("Select one in the following: ")
print("1. Month calendar?")
print("2. Whole year calendar?")

choice = input("Enter a choice 1/2: ")

if (choice == '1'):
	print(calendar.month(yy,mm))

else:
	print(calendar.prcal(yy))