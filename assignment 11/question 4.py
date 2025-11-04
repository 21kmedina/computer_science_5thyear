'''
author: Karla Patino Medina
date: 4th November 2025
assignment 11 question 4
'''
number=80
tries=7
while tries!=0:
    guess=input('Enter your guess:')
    guess=int(guess)
    if guess==number:      
        print('CORRECT')
        break
    elif guess<number:
        print('Too low')
        tries-=1
    elif guess>number:
        print('Too high')
        tries-=1
    
