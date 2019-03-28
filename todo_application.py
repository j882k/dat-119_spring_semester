# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 18:07:38 2019

@author: jakej
"""

def menu():
    print("1. View the items on your todo list")
    print('2. View the items you have finished')
    print('3. Add items to your todo list')
    print('4. Mark a todo list item as completed')
    print('5. Exit the todo list application (list will not be saved)')
    print('')
    select = int(input('please select one of the options above (numbers only): '))
    if select == 1:
        keep_going = view_items()
    elif select == 2:
        keep_going = view_finished()
    elif select == 3:
        keep_going = add_items()
    elif select == 4:
        keep_going = todo_finished()
    elif select == 5:
        keep_going = big_exit()
    else:
        print("invalid response")
        keep_going = 6
        return keep_going
    return keep_going

def view_items():
    count = 0
    for items in todo:
        count = count + 1
        print(count,')', items)
    leave = input('press "enter" to continue: ')
    if leave == 'n':
        keep_going = 6
        return keep_going
    else:
        keep_going = 6
        return keep_going

def view_finished():
    count = 0
    for items in finished:
        count = count + 1
        print(count, ')', items)
    leave = input('press "enter" to continue: ')
    if leave == 'n':
        keep_going = 6
        return keep_going
    else:
        keep_going = 6
        return keep_going
        
def add_items():
    repeat = 6
    while repeat == 6:
        addition = input('please enter the task you would like to add: ')
        todo.append(addition)
        leave = input("would you like to add another item? (y for yes and n for no): ")
        if leave == 'y':
            repeat = 6
        elif leave == 'n':
            keep_going = 6
            return keep_going
        else:
            print("invalid response")
            keep_going = 6
            return keep_going

def todo_finished():
    repeat = 6
    while repeat == 6:
        count = 0
        for items in todo:
            count = count + 1
            print(count,')',items)
        print('')
        finish = input('please enter the task in which you finished: ')
        todo.remove(finish)
        finished.append(finish)
        leave = input('would you like to mark another item as finished (y for yes, n for no): ')
        if leave == 'y':
            repeat = 6
        elif leave == 'n':
            keep_going = 6
            return keep_going
        else:
            print("invalid response")
            keep_going = 6
            return keep_going
                
def big_exit():
    print('')
    print('Thank you!')
    keep_going = 5
    return keep_going
    
    
global todo
todo=[]
global finished
finished=[]
global keep_going
keep_going = 6
while keep_going == 6:
    keep_going = menu()