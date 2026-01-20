'''
Author:Karla Patino Medina
Date: 20/01/2026
About: Programming practice TYPE C
'''
#1
lst2=[]
lst=[1, 2, 3]
print(f'This is the list,{lst},')
num=input('Enter a digit to increment list by :')
num=int(num)
for i in lst:
    i=i+num
    lst2.append(i)
print(lst2)
    
