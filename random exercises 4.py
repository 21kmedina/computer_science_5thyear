'''
author:karla patino
date:09/02/2026
importing random exercises question 4
'''
import random

randnum=random.randint(1,100)
guess=7
while guess!=0:
    Userguess=input('Guess the number between 1 and 100 :')
    guess-=1
    Userguess=int(Userguess)
    if Userguess==randnum:
        print('Success')
        break
    elif Userguess!=randnum:
        print('Try again')
if guess==0:
    print('failed')
        
        