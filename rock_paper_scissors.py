# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 20:10:04 2019

@author: jakej
"""
import random
ai=int
repeat = int
ready = input("Are you ready to play? (y for yes, n for no): ")
if ready == 'y':
    repeat = 6
else:
    print("Take your time.")
#get the human guess#
while repeat == 6:
 user=input("rock, paper, or scissors?: ")
#get the ai guess#
 def getAI(ai):
     if ai ==1:
        computer = 'rock'
     elif ai == 2:
        computer = 'paper'
     elif ai == 3:
        computer = 'scissors'
     return computer
 computer = getAI(random.randint(1,3))
#compute results with IF statements
 if computer == 'rock' and user == 'rock':
     print("Computer chose rock!")
     print("it's a tie!")
 elif computer == 'paper' and user == 'paper':
     print("Computer chose paper!")
     print("it's a tie!")
 elif computer == 'scissors' and user == 'scissors':
     print("Computer chose scissors!")
     print("it's a tie!")
 elif computer == 'rock' and user == 'scissors':
     print("Computer chose rock!")
     print("You lost, sorry.")
 elif computer == 'rock' and user == 'paper':
     print("Computer chose rock!")
     print("You won, Congratulations!")
 elif computer == 'scissors' and user == 'rock':
     print("Computer chose scissors!")
     print("You won, Congratulations!")
 elif computer == 'scissors' and user == 'paper':
     print("Computer chose scissors")
     print("You lost, sorry.")
 elif computer == 'paper' and user == 'scissors':
     print("Computer chose paper!")
     print("You won, congratulations!")
 elif computer == 'paper' and user == 'rock':
     print("Computer chose paper!")
     print("You lost, sorry.")
 else:
    print("Invalid response, please try again.")
 restart = input("would you like to try again?(y for yes, n for no): ")
 if restart == 'y':
     repeat == 6
 else:
     print("Thank you!")