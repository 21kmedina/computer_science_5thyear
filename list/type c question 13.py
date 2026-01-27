'''
Author:Karla Patino Medina
Date: 27/01/2026
About: Programming practice TYPE C, question 13
'''
lst=eval(input('Enter a list :'))
small_index=eval(input('Enter the smallest index :'))

big_index=eval(input('Enter the biggest index :'))
new_lst=lst[small_index:big_index]

print('min value is :',min(new_lst),'max value is :',max(new_lst))

