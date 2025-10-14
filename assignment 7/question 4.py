'''
Karla Patino Medina
14th October 2025
assignment 7, question 4
convert decimal to binary

'''


y=input('enter a number to turn it to decimal:')
y=int(y)
while y!=0:
    remainder=y%2
    y=y//2
    print(remainder)

    

