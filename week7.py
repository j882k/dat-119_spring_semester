# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 18:34:10 2019

@author: jakej
"""
list1=['games','sports','animals','movies','sleep','work','school']
number = int(input('please pick a number between 0 and 6: '))
print('the item you have slected is:', list1[number])
print("----------------------------------------")
print("the first three items on this list are:")
for words in list1[0:3]:
    print("-", words)
print("----------------------------------------")
print("the last three items on this list are:")
for words in list1[-3:]:
    print("-", words)
print("----------------------------------------")
new=input("type a new word you would like to add to the list: ")
list1.append(new)
print("----------------------------------------")
print("The list is now alphabetical")
list1.sort()
print("----------------------------------------")
print("Here is your updated list:")
for words in list1:
    print("-", words)
remove=input("What is your least favorite item on the list?: ")
list1.remove(remove)
print("----------------------------------------")
print("Final copy of the list:")
for words in list1:
    print("-", words)
