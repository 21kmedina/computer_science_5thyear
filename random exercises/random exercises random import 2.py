'''
author:karla patino
date:09/02/2026
importing random exercises 2
'''
print('Welcome to my dice game!!')
import random
User_name=input('Please enter your name :')
User_name=User_name+'s'

lucky_number=input('Please select a lucky number between 1 and 6:')
lucky_number=int(lucky_number)

print(User_name,'lucky number is:',lucky_number)

computer_die_roll=random.randint(1,6) #initialize computer number
print('the computer rolled:',computer_die_roll)

if lucky_number==computer_die_roll:
    print('you guessed correct, Well done!!')
elif lucky_number>computer_die_roll:
    print('You guessed too high!')
elif lucky_number<computer_die_roll:
    print('You guessed too low!!')
    