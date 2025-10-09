'''
Karla Patino Medina
9th October 2025
assignment 6, question 8


'''

num=7
guess=0

while num!='':
    guess=int(input('Enter you guess of what my number is:'))
    if (guess==num):
        print('YOU GUESSED CORRECTLY!!')
        break
    elif(guess>num):
        print('too high ):')
    elif(guess<num):
        print('too lowww ):')
