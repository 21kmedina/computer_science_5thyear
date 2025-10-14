'''
Karla Patino Medina
14th October 2025
assignment 7, question 3
convert binary to decimal

'''


y=input('enter a number to turn it to decimal:')
y=int(y)
while y!=0:
    remainder=y%2
    y=y//2
    print(remainder)
    