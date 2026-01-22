'''
Author:Karla Patino Medina
Date: 20/01/2026
About: Programming practice TYPE C, question 6
'''
#6
num=8
user_lst=eval(input('Enter a list :'))
for i in user_lst:
    if i==num:
        index=user_lst.index(i)
        print ('number is present at position',index)
    elif i!=num:        
        print('Number is NOT present in list',user_lst)

