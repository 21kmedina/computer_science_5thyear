'''
Author:Karla Patino Medina
Date: 26/01/2026
About: Programming practice TYPE C, question 9
'''

User_input=eval(input('Enter a value to find out the fibonacci series value :'))

lst=[0,1]

for i in range(0,User_input-1):
    total=lst[-2]+lst[-1]
    lst.append(total)
print(lst[-1])

