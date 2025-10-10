'''
Karla Patino Medina
10th October 2025
assignment 7, question 1
program checking for armstrong numbers


'''
num=0
total=0
num=input('enter a number :')
power=len(num)
for digit in num:
    total=total+ int(digit)**power
if total==int(num):
    print('that is an armstrong number')
else:
    print('thats not an armstrong number')
