# -*- coding: utf-8 -*-
"""
Created on Wed May  1 18:09:22 2019

@author: jakej
"""
import random
number = int
cards = {'ace of clubs':number,
         'ace of hearts':number,
         'ace of spades':number,
         'ace of diamonds':number,
         'two of clubs':2,
         'two of hearts':2,
         'two of spades':2,
         'two of diamonds':2,
         'three of clubs':3,
         'three of hearts':3,
         'three of spades':3,
         'three of diamonds':3,
         'four of clubs':4,
         'four of hearts':4,
         'four of spades':4,
         'four of diamonds':4,
         'five of clubs':5,
         'five of hearts':5,
         'five of spades':5,
         'five of diamonds':5,
         'six of clubs':6,
         'six of hearts':6,
         'six of spades':6,
         'six of diamonds':6,
         'seven of clubs':7,
         'seven of hearts':7,
         'seven of spades':7,
         'seven of diamonds':7,
         'eight of clubs':8,
         'eight of hearts':8,
         'eight of spades':8,
         'eight of diamonds':8,
         'nine of clubs':9,
         'nine of hearts':9,
         'nine of spades':9,
         'nine of diamonds':9,
         'ten of clubs':10,
         'ten of hearts':10,
         'ten of spades':10,
         'ten of diamonds':10,
         'jack of clubs':10,
         'jack of hearts':10,
         'jack of spades':10,
         'jack of diamonds':10,
         'queen of clubs':10,
         'queen of hearts':10,
         'queen of spades':10,
         'queen of diamonds':10,
         'king of clubs':10,
         'king of hearts':10,
         'king of spades':10,
         'king of diamonds':10}
def menu():
    keep_going = 6
    while keep_going == 6:
        print('')
        print('')
        print('Game menu')
        print('1: view card list')
        print('2: view game rules')
        print('3: play against AI')
        print('4: play against another player')
        print('5: exit game')
        selection = input('please enter the number of your selection: ')
        if selection == '1':
            cardList()
        elif selection == '2':
            rules()
        elif selection == '3':
            solo()
        elif selection == '4':
            pvp()
        else:
            print('gg')
            keep_going = 0

def solo():
   PersonCount = 0
   CompCount = 0
   replay = 6
   while replay == 6:
    Prand1=random.choice(list(cards))
    card1 = cards[Prand1]
    print("your first card is a",Prand1)
    if Prand1=='ace of clubs' or Prand1=='ace of hearts' or Prand1=='ace of spades' or Prand1=='ace of diamonds':
        card1 = int(input('would you like your ace to be worth 11 or 1: '))
        if card1 > 1 and card1 < 11:
            print('invalid response')
            solo()
    print('')
    Prand2=random.choice(list(cards))
    card2 = cards[Prand2]
    print('your second card is a',Prand2)    
    if Prand2=='ace of clubs' or Prand2=='ace of hearts' or Prand2=='ace of spades' or Prand2=='ace of diamonds':
        card2 = int(input('would you like your ace to be worth 11 or 1: '))
        if card2 > 1 and card2 < 11:
            print('invalid response')
            solo()
    Pdraw = (card1+card2)
    print('')
    print('these total to',Pdraw)
    if Pdraw > 21:
        print('so you get a redraw')
        print('')
        solo()
    hit=input('press h for hit or d for done: ')
    redo = 6
    if hit == 'h':
        print('')
        while redo == 6:
            Prand3 = random.choice(list(cards))
            card3 = cards[Prand3]
            if Prand3=='ace of clubs' or Prand3=='ace of hearts' or Prand3=='ace of spades' or Prand3=='ace of diamonds':
                card3 = int(input('would you like your ace to be worth 11 or 1: '))
                if card3 > 1 and card3 < 11:
                    print('invalid response')
                    redo = 6
            print('invalid response')    
            Pdraw = Pdraw + card3
            print('you have drawn a',Prand3)
            print('This is worth',card3)
            print('')
            print('your total is',Pdraw)
            if Pdraw > 21:
                print('You have gone over 21, your entry goes as DNF')
                Pdraw = 0
                redo = 0
                again = 'd'
            else:
                print('')
                again = input('press h for hit or d for done: ')
                if again == 'h':
                    redo = 6
                else:
                    redo = 0
    print('')
    print('your total comes to',Pdraw,'which is',(21-Pdraw),'away from 21')
    print("it's the computer's turn to play!")
    print('')
    Arand1=random.choice(list(cards))
    if Arand1=='ace of clubs' or Arand1=='ace of hearts' or Arand1=='ace of spades' or Arand1=='ace of diamonds':
        Acard1 = 11
    else:
        Acard1=cards[Arand1]
    print('Computer drew a', Arand1, 'which is worth', Acard1)
    Arand2 = random.choice(list(cards))
    Acard2 = cards[Arand2]
    if Arand2=='ace of clubs' or Arand2=='ace of hearts' or Arand2=='ace of spades' or Arand2=='ace of diamonds':
        if Acard1 == 11:
            Acard2 = 1
        else:
            Acard2 = 11
    print('Computer drew a', Arand2, 'which is worth', Acard2)
    print('')
    Adraw = (Acard1 + Acard2)
    print('These total to', Adraw)
    auto = 6
    while auto == 6:
        if Adraw < Pdraw:
            Arand3 = random.choice(list(cards))
            Acard3 = cards[Arand3]
            if Arand3=='ace of clubs' or Arand3=='ace of hearts' or Arand3=='ace of spades' or Arand3=='ace of diamonds':
                if Adraw > 10:
                    Acard3 = 1
                else:
                    Acard3 = 11
            print('the computer has taken a hit and draw a', Arand3, 'worth', Acard3)
            Adraw = Adraw + Acard3
            if Adraw > 21:
                print("The computer has gone over 21!")
                Adraw = 0
                auto = 0
            elif Adraw <21 and Adraw > Pdraw:
                Adraw = Adraw
            else:
                auto = 6
        else:
            Adraw = Adraw
            auto = 0
    print('The computer totals to', Adraw, 'which is', (21-Adraw), 'away from 21.')
    print('')
    if (21-Pdraw) > (21-Adraw):
        print('The computer has won this match')
        CompCount = CompCount + 1
    elif (21-Pdraw) < (21-Adraw):
        print('You have won this match!')
        PersonCount = PersonCount + 1
    else:
        print('This match is a draw')
    print('')
    playagain = input('Would you like to play again?(y for yes, n for no): ')
    if playagain == 'y':
        replay = 6
    elif playagain =='n':
        print('Thanks for playing')
        print("your win total is", PersonCount, "to the computer's", CompCount, "wins.")
        replay = 0
        keep_going = 6
        return keep_going
    else:
        print('Thanks for playing')
        print("your win total is", PersonCount, "to the computer's", CompCount, "wins.")
        replay = 0
        keep_going = 6
        return keep_going

def rules():
    print('rules')
    print('you will draw 2 cards worth their designated amounts')
    print('if an ace is drawn, the player will get to choose a value, either 1 or 11')
    print('you will then get the option to "hit" or "draw"')
    print('the goal is to get your amount as close to 21 as possible without going over')
    print('you can get as many hits as you like until you exceed 21')
    print('the player with the closest number to 21 wins the match')
    print(':')
    print(':')
    men = input('press enter to return to menu: ')
    if men == '':
        keep_going = 6
    else:
        keep_going = 6
    return keep_going
def cardList():
    print('ace of clubs: 1 or 11')
    print('ace of hearts: 1 or 11')
    print('ace of spades: 1 or 11')
    print('ace of diamonds: 1 or 11')
    print('two of clubs: 2')
    print('two of hearts: 2')
    print('two of spades: 2')
    print('two of diamonds: 2')
    print('three of clubs: 3')
    print('three of hearts: 3')
    print('three of spades: 3')
    print('three of diamonds: 3')
    print('four of clubs: 4')
    print('four of hearts: 4')
    print('four of spades: 4')
    print('four of diamonds: 4')
    print('five of clubs: 5')
    print('five of hearts: 5')
    print('five of spades: 5')
    print('five of diamonds: 5')
    print('six of clubs: 6')
    print('six of hearts: 6')
    print('six of spades: 6')
    print('six of diamonds: 6')
    print('seven of clubs: 7')
    print('seven of hearts: 7')
    print('seven of spades: 7')
    print('seven of diamonds: 7')
    print('eight of clubs: 8')
    print('eight of hearts: 8')
    print('eight of spades: 8')
    print('eight of diamonds: 8')
    print('nine of clubs: 9')
    print('nine of hearts: 9')
    print('nine of spades: 9')
    print('nine of diamonds: 9')
    print('ten of clubs: 10')
    print('ten of hearts: 10')
    print('ten of spades: 10')
    print('ten of diamonds: 10')
    print('jack of clubs: 10')
    print('jack of hearts: 10')
    print('jack of spades: 10')
    print('jack of diamonds: 10')
    print('queen of clubs: 10')
    print('queen of hearts: 10')
    print('queen of spades: 10')
    print('queen of diamonds: 10')
    print('king of clubs: 10')
    print('king of hearts: 10')
    print('king of spades: 10')
    print('king of diamonds: 10')
    print(':')
    print(':')
    ye = input('press enter to return to menu: ')
    if ye == '':
        keep_going = 6
    else:
        keep_going = 6
    return keep_going
def pvp():
   Playercount = 0
   Player2Count = 0
   replay = 6
   while replay == 6:
    Prand1=random.choice(list(cards))
    card1 = cards[Prand1]
    print("your first card is a",Prand1)
    if Prand1=='ace of clubs' or Prand1=='ace of hearts' or Prand1=='ace of spades' or Prand1=='ace of diamonds':
        card1 = int(input('would you like your ace to be worth 11 or 1: '))
        if card1 > 1 and card1 < 11:
            print('invalid response')
            solo()
    print('')
    Prand2=random.choice(list(cards))
    card2 = cards[Prand2]
    print('your second card is a',Prand2)    
    if Prand2=='ace of clubs' or Prand2=='ace of hearts' or Prand2=='ace of spades' or Prand2=='ace of diamonds':
        card2 = int(input('would you like your ace to be worth 11 or 1: '))
        if card2 > 1 and card2 < 11:
            print('invalid response')
            solo()
    Pdraw = (card1+card2)
    print('')
    print('these total to',Pdraw)
    if Pdraw > 21:
        print('so you get a redraw')
        print('')
        solo()
    hit=input('press h for hit or d for done: ')
    redo = 6
    if hit == 'h':
        print('')
        while redo == 6:
            Prand3 = random.choice(list(cards))
            card3 = cards[Prand3]
            if Prand3=='ace of clubs' or Prand3=='ace of hearts' or Prand3=='ace of spades' or Prand3=='ace of diamonds':
                card3 = int(input('would you like your ace to be worth 11 or 1: '))
                if card3 > 1 and card3 < 11:
                    print('invalid response')
                    redo = 6
            print('invalid response')    
            Pdraw = Pdraw + card3
            print('you have drawn a',Prand3)
            print('This is worth',card3)
            print('')
            print('your total is',Pdraw)
            if Pdraw > 21:
                print('You have gone over 21, your entry goes as DNF')
                Pdraw = 0
                redo = 0
                again = 'd'
            else:
                print('')
                again = input('press h for hit or d for done: ')
                if again == 'h':
                    redo = 6
                else:
                    redo = 0
    print('')
    print('your total comes to',Pdraw,'which is',(21-Pdraw),'away from 21')
    print('')
    print('It is player 2s turn to play!')
    Prand4=random.choice(list(cards))
    card4 = cards[Prand4]
    print("your first card is a",Prand4)
    if Prand4=='ace of clubs' or Prand4=='ace of hearts' or Prand4=='ace of spades' or Prand4=='ace of diamonds':
        card4 = int(input('would you like your ace to be worth 11 or 1: '))
        if card4 > 1 and card4 < 11:
            print('invalid response')
            replay=6
    print('')
    Prand5=random.choice(list(cards))
    card5 = cards[Prand5]
    print('your second card is a',Prand5)    
    if Prand5=='ace of clubs' or Prand5=='ace of hearts' or Prand5=='ace of spades' or Prand5=='ace of diamonds':
        card5 = int(input('would you like your ace to be worth 11 or 1: '))
        if card5 > 1 and card5 < 11:
            print('invalid response')
            replay = 6
    Pdraw2 = (card4+card5)
    print('')
    print('these total to',Pdraw2)
    if Pdraw2 > 21:
        print('so you get a redraw')
        print('')
        solo()
    hit=input('press h for hit or d for done: ')
    redo = 6
    if hit == 'h':
        print('')
        while redo == 6:
            Prand6 = random.choice(list(cards))
            card6 = cards[Prand6]
            if Prand6=='ace of clubs' or Prand6=='ace of hearts' or Prand6=='ace of spades' or Prand6=='ace of diamonds':
                card6 = int(input('would you like your ace to be worth 11 or 1: '))
                if card6 > 1 and card6 < 11:
                    print('invalid response')
                    redo = 6
            print('invalid response')    
            Pdraw2 = Pdraw2 + card6
            print('you have drawn a',Prand6)
            print('This is worth',card6)
            print('')
            print('your total is',Pdraw2)
            if Pdraw2 > 21:
                print('You have gone over 21, your entry goes as DNF')
                Pdraw2 = 0
                redo = 0
                again = 'd'
            else:
                print('')
                again = input('press h for hit or d for done: ')
                if again == 'h':
                    redo = 6
                else:
                    redo = 0
    print('')
    print('your total comes to',Pdraw2,'which is',(21-Pdraw2),'away from 21')
    if (21-Pdraw)>(21-Pdraw2):
        print('Player 2 has won this game!')
        Player2Count=Player2Count + 1
    elif (21-Pdraw) < (21-Pdraw2):
        print('Player 1 has won this game!')
        Playercount = Playercount + 1
    else:
        print('This match results in a tie')
    yes = input('would you like to play again?(y for yes, n for no): ')
    if yes == 'y':
        replay = 6
    elif yes == 'n':
        print('thanks for playing')
        print("Player 1 won", Playercount, "games to Player 2's", Player2Count, "wins.")
        keep_going = 6
        return keep_going
    else:
        print('thanks for playing')
        print("Player 1 won", Playercount, "games to Player 2's", Player2Count, "wins.")
        keep_going = 6
        return keep_going

print('Welcome to Python BlackJack!')
menu()