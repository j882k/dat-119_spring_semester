# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 18:38:53 2019

@author: jakej
"""
repeat = 6
while repeat == 6:
    string = input("Please enter a word or phrase: ")
    string = string.replace(" ","")
    string = string.lower()
    string = string.replace('?','')
    string = string.replace('!','')
    string = string.replace('-','')
    string = string.replace('.','')
    string = string.replace(',','')
    string = string.replace("'","")
    new_string = string[::-1]
    if string == new_string:
        print("this is indeed a palinome, very cool")
    else:
        print("this is not a palinome, you're done")
    again = input('want to go again? (n for no, y for yes): ')
    if again == 'y':
        repeat = 6
    elif again == 'n':
        print('ok man')
        repeat = 0
    else:
        print('invalid answer')
        repeat = 0
