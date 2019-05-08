# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 19:46:17 2019

@author: jakej
"""

story = open('prejudice(1).txt','r')
stories = story.read()
print("I will count each vowel inside of this story for you")
print("Here is your story:")
print(stories)
counta = -1
counte = -1
counti = -1
counto = -1
countu = -1
countA = -1
countE = -1
countI = -1
countO = -1
countU = -1
a = stories.split('a')
for splits in a:
    counta = counta + 1
A = stories.split('A')
for splits in A:
    countA = countA + 1
e = stories.split('e')
for splits in e:
    counte = counte + 1
E = stories.split('E')
for splits in E:
    countE = countE + 1
i = stories.split('i')
for splits in i:
    counti = counti + 1
I = stories.split('I')
for splits in I:
    countI = countI + 1
o = stories.split('o')
for splits in o:
    counto = counto + 1
O = stories.split('O')
for splits in O:
    countO = countO + 1
u = stories.split('u')
for splits in u:
    countu = countu + 1
U = stories.split('U')
for splits in U:
    countU = countU + 1
print('---------------------------------')
print('the letter A appears', counta + countA, 'times in this story.')
print('---------------------------------')
print('the letter E appears', counte + countE, 'times in this story.')
print('---------------------------------')
print('the letter I appears', counti + countI, 'times in this story.')
print('---------------------------------')
print('the letter O appears', counto + countO, 'times in this story.')
print('---------------------------------')
print('the letter U appears', countu + countU, 'times in this story.')
print('---------------------------------')
print('thank you')
