'''
Karla Patino Medina
7th October 2025
assignment 6, qsnt 4
print number fron 0-number, skip multiples of 5

'''
num=-0
while num!='':
    num=input('enter a number :')
    if num.isdigit():
        num=int(num)
        for i in range(0,num):
            if(i%5 == 0):
                continue
            print(i)
                 