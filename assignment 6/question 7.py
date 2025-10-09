'''
Karla Patino Medina
9th October 2025
assignment 6, question 7


'''
num=0
while num !='':
    num=input('enter a number between 10 and 20: ')
    if num.isdigit():
        num=int(num)
        if(num >=10) and (num<=20):
            print('thank you')
            break
        elif(num<10):
            print('too low')
        elif(num<20):
            print('too high')
else:
    print('you did something wrong')
        