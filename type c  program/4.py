'''
Author:Karla Patino Medina
Date: 20/01/2026
About: Programming practice TYPE C, question 4
'''
user_lst=eval(input('Enter a list containing numbers from 1 to 12: '))
lst2=[]

for i in user_lst:
    if i > 10:
        i=10
    lst2.append(i)
print(lst2)
        
