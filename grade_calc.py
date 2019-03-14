# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 16:21:59 2019

@author: jakej
"""
total = 0
counter = 0
print("hello, I will average your grades")
again=input("do you need anymore grades inputed? (y for yes, n for no): ")
while again == 'y':
    grade = int(input("please enter your grade: "))
    if grade <=100 and grade >= 0:
        total = total + grade
        counter = counter + 1
        again = input("do you need anymore grades inputed? (y for yes, n for no): ")
        if again == 'n':
            print('you entered', counter, 'grades')
            total_avg = (total / counter)
            print("Overall Average is", total_avg)
    else:
        print("Please enter a valid grade")
print("thank you")

