# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 20:07:14 2019

@author: jakej
"""
import random
state_dictionary = {'Alabama':'Montgomery',
                    'Alaska':'Juneau',
                    'Arizona':'Phoenix',
                    'Arkansas':'LittleRock',
                    'California':'Sacramento',
                    'Colorado':'Denver',
                    'Connecticut':'Hartford',
                    'Delaware':'Dover',
                    'Florida':'tallahassee',
                    'Georgia':'Atlanta',
                    'Hawaii':'Honolulu',
                    'Idaho':'Boise',
                    'Illinois':'Springfield',
                    'Indiana':'Indianapolis',
                    'Iowa':'DesMoines',
                    'Kansas':'Topeka',
                    'Kentucky':'Frankfort',
                    'Louisiana':'BatonRouge',
                    'Maryland':'Annapolis',
                    'Massachusetts':'Boston',
                    'Michigan':'Lansing',
                    'Minnesota':'SaintPaul',
                    'Mississippi':'Jackson',
                    'Missouri':'JeffersonCity',
                    'Montana':'Helena',
                    'Nebraska':'Lincoln',
                    'Nevada':'CarsonCity',
                    'NewHampshire':'Concord',
                    'NewJersey':'Trenton',
                    'NewMexico':'SantaFe',
                    'NewYork': 'Albany',
                    'NorthCarolina':'Raleigh',
                    'NorthDakota':'Bismarck',
                    'Ohio':'Columbus',
                    'Oklahoma':'OklahomaCity',
                    'Oregon':'Salem',
                    'Pennsylvania':'Harrisburg',
                    'RhodeIsland':'Providence',
                    'SouthCarolina': 'Columbia',
                    'SouthDakota':'Pierre',
                    'Tennessee':'Nashville',
                    'Texas':'Austin',
                    'Utah':'SaltLakeCity',
                    'Vermont': 'Montpelier',
                    'Virginia':'Richmond',
                    'Washington':'Olympia',
                    'WestVirginia': 'Charleston',
                    'Wisconsin':'Madison',
                    'Wyoming':'Cheyenne'}
redo = 6
while redo == 6:
    print("what is the capital of this state?")
    state = (random.choice(list(state_dictionary)))
    print(state)
    capAnswer = input('Capital: ')
    if capAnswer == state_dictionary[state]:
        print("Yes that is correct")
    else:
        print("Naw Dawg")
    repeat = input("would you like to play again (yes or no): ")
    if repeat == 'yes':
        redo = 6
    elif repeat == 'no':
        print("dang alright")
        redo = 0
    else:
        print('incorrect response')
        redo = 0
    
    


