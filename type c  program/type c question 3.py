'''
Author:Karla Patino Medina
Date: 20/01/2026
About: Programming practice TYPE C, question 3
'''
#3
lst3=[]
lst1=input('Enter a list: ')
lst2=input('Enter a list: ')
lst1=list(lst1)
lst2=list(lst2)
lst1.extend(lst2)
lst3.extend(lst1)
print(lst3)