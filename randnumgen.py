# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 14:24:24 2019

@author: jakej
"""
import random
def getNum(number):
    number=random.randint(1,100)
    return number
def getGuess(guess):
    guess=int(input("What is your guess?: "))
    return guess
again = 5
while again == 5:
 print("The computer will generate a random number between 1 and 100.")
 print("Your task is to guess that number, you have unlimited guesses.")
 number = int
 number = getNum(number)
 print("The computer's number is in!")
 repeat = 6
 count = 0
 while repeat == 6:
    count = count + 1
    guess = int
    guess = getGuess(guess)
    if guess > number:
        print("Your guess is too high, try again.")
        repeat = 6
    elif guess < number:
        print("Your guess is too low, try again.")
        repeat = 6
    elif guess == number:
        print('congrats, you guessed the number!')
        repeat = 0
 print("you took", count, "guesses")
 playAgain = input("would you like to play again?(y for yes, n for no): ")
 if playAgain == 'y':
     again = 5
 elif playAgain == 'n':
     print("Thanks for playing!")
     again = 0
 else:
     print("invalid answer")
     again = 0
 

