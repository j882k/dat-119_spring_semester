# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 16:36:57 2019

@author: jakej
"""
yes = open('prejudice(1).txt','r')
no = open('prejudice_latin.txt','w')
original = yes.readlines()
list_of_words=[]

for line in original:
    bad_word = line.split('_')
    for a_line in bad_word:
        list_of_words = list_of_words + a_line.split(' ')
while ' ' in list_of_words:
    list_of_words.remove(' ')
for index in range(0, len(list_of_words)):
    list_of_words[index] = list_of_words[index].strip('\n')
    list_of_words[index] = list_of_words[index].strip(';')
    list_of_words[index] = list_of_words[index].strip('.')
    list_of_words[index] = list_of_words[index].strip(',')
    list_of_words[index] = list_of_words[index].strip('!')
    list_of_words[index] = list_of_words[index].strip('?')
    list_of_words[index] = list_of_words[index].strip('"')
while '' in list_of_words:
    list_of_words.remove('')
for words in list_of_words:
    word = words.replace(words[0],'')
    help_me = (word,words[0],'ay')
    no.write(help_me)
no.close()
yes.close()



        
        


    
    
