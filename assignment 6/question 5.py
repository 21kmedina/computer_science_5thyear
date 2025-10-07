'''
Karla Patino Medina
7th October 2025
assignment 6, qsnt 5


'''
num=1
while num!='':
    num=input('enter a number :')
    if num.isdigit():
        num=int(num)
        for i in range(0,num*num):
           # if(i%2 == 0):
                print(i)