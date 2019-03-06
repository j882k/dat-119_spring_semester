# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 20:16:39 2019

@author: jakej
"""

year=int(input("I am a leap year calculator, please enter a year (AD): "))
if year % 400 == 0:
    print("This year is a leap year, there was/will be 29 days in February")
elif year % 4 > 0 or year % 100 == 0:    
    print("This year is not a leap year, there was/will be 28 days in February")
elif year % 4 == 0 and year >= 0 and year % 100 > 0:
    print("This year is a leap year, there was/will be 29 days in February")
else:
    print("invalid year, please try again")
print("Thank you")