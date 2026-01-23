'''
Author:Karla Patino Medina
Date: 20/01/2026
About: Programming practice TYPE C, question 7
'''
#Q7 a
lst=[]
for i in range(0,50,1):
    lst.append(i)
print(lst)

#part 7 b
lst2=[]
for i in range(0,51):
    x=i**2
    lst2.append(x)
print(lst2)

#part c,7
increase=1
lst3=[]
lst1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
for i in lst1:
    i=i*increase
    lst3.append(i)
    increase+=1
print(lst3)
    
