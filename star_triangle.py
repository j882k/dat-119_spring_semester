# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 14:41:07 2019

@author: jakej
"""
yes=int
def pyramid_build():
    base=int(input("How big would you like your base to be?: "))
    if base > 0:
        for r in range(base):
            for c in range(r+1):
                print("*",end='')
            print()
    else:
        print("number invalid, please restart")
print("let's build a triangle!")
pyramid_build()
yes = 6
while yes == 6:
    rep=input("Would you like to build again? (y for yes, n for no): ")
    if rep == 'y':
        pyramid_build()
        yes = 6
    else:
            print("Thank you!")
            yes = 0
