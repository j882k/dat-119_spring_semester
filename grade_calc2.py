# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 16:21:59 2019

@author: jakej
"""
total = 0
counter = 0
print("hello, I will average your grades")
again=input("enter y to begin grade entries: ")
while again == 'y':
    grade =int(input("please enter your grade(or enter '101' to calculate entries thus far): "))
    if grade <=100 and grade >= 0:
        total = total + grade
        counter = counter + 1
    elif grade == 101:
            print('you entered', counter, 'grades')
            total_avg = (total / counter)
            print("Overall Average is", total_avg)
    else:
        print("Please enter a valid grade")
print("thank you")

