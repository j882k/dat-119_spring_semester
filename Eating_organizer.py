# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 13:26:19 2019

@author: jakej
"""

print("I will tell you what places you can eat at with your guests.")
veg=input("Are any of your friends vegetarian? (y for yes, n for no): ")
if veg == 'y' or veg == 'n':
    glut=input("Are any of your friends Gluten Free? (y for yes, n for no): ")
    if glut == 'y' or glut =='n':
        vegan=input("Are any of your friends Vegan? (y for yes, n for no): ")
        if veg == 'n' and glut == 'n' and vegan == 'n':
            print("you can eat anywhere")
        elif veg == 'y' and glut == 'n' and vegan == 'n':
            print("Main street pizza company")
            print("Corner Cafe")
            print("Mama's Fine Italian")
            print("The Chef's Kitchen")
        elif veg == 'y' and glut == 'y' and vegan == 'n':
            print("Main Street Pizza Company")
            print("Corner Cafe")
            print("The Chef's Kitchen")
        elif veg == 'y' and glut == 'n' and vegan == 'y':
            print("Corner Cafe")
            print("Chef's Kitchen")
        elif veg == 'n' and glut == 'y' and vegan =='y':
            print("Corner Cafe")
            print("The Chef's Kitchen")
        elif veg == 'n' and glut == 'n' and vegan == 'y':
            print("Corner Cafe")
            print("The Chef's Kitchen")
        elif veg == 'n' and glut == 'y' and vegan == 'n':
            print("Main Street Pizza Company")
            print("Corner Cafe")
            print("The Chef's Kitchen")
        else:
            print("Corner Cafe")
            print("The Chef's Kithen")
    else:
        print("invalid answer please go back and answer again")
else:
    print("invalid answer, please reread the question and answer again")
print("Thank you")
