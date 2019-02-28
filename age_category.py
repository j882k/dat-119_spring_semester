# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 19:43:38 2019

@author: jakej
"""

age=int(input("how old is your child: "))
if age == 0 or age == 1:
    print("your kid is an infant")
elif age > 1 and age < 13:
    print("your kid is a child")
elif age >=13 and age < 20:
    print("your kid is a teenager")
elif age >= 20:
    print("your kid is an adult")
else:
    print("Please enter a valid age.")