'''
Author:Karla Patino Medina
Date: 23/01/2026
About: Programming practice TYPE C, question 8
'''

lst_m=eval(input('Enter valus for list M :'))
lst_m=list(lst_m)

lst_L=eval(input('Enter valus for list L same amount as list m :'))
lst_L=list(lst_L)

lst_n=[]
if len(lst_m)==len(lst_L):
    length_both=len(lst_m)
    
    for i in range (0,length_both):
        lst_n.append(lst_m[i]+lst_L[i])
    print(lst_n)
    
elif len(lst_m)!=len(lst_L):
    print('the lenghts are not equal')
     
