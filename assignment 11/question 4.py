'''
author: Karla Patino medina
date: 3rd november 2025
assignment 11 queston 4
'''
number=80
tries=7
while tries!='':
    guess=input('Enter your guess:')
    guess=int(guess)
    if guess==number:      
        print('CORRECT')
    elif guess<number:
        print('Too low')
        tries=-1
    elif guess>number:
        print('Too high')
        tries=-1
    