# -*- coding: utf-8 -*-
"""
Created on Wed May  1 16:27:33 2019

@author: jakej
"""

letters={'a':0,
         'b':0,
         'c':0,
         'd':0,
         'e':0,
         'f':0,
         'g':0,
         'h':0,
         'i':0,
         'j':0,
         'k':0,
         'l':0,
         'm':0,
         'n':0,
         'o':0,
         'p':0,
         'q':0,
         'r':0,
         's':0,
         't':0,
         'u':0,
         'v':0,
         'w':0,
         'x':0,
         'y':0,
         'z':0}
redo = 6
while redo == 6:
    sentence = input('enter any sentence and I will count the letters: ')
    print(sentence)
    sentences=sentence.lower()
    sentences = sentences.replace(' ','')
    sentences = sentences.replace("'","")
    sentences = sentences.replace('?','')
    sentences = sentences.replace('!','')
    sentences = sentences.replace('.','')
    sentences = sentences.replace(',','')
    for letter in sentences:
        letters[letter] = letters[letter] + 1
    print(letters)
    replay = input('Would you like to go again? (yes or no): ')
    if replay == 'yes':
        redo = 6
    elif replay == 'no':
        print("thanks for playing")
        redo = 0
    else:
        print('invalid input')
        redo = 0
    
