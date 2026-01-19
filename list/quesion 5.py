'''
Name:Karla Patino
Date:15/01/2026
excersises from book 
'''

#Q5
x=['3','2','5']
y=''
while x:
    y=y+x[-1]
    x=x[:len(x)-1]
print(y)
print(x)
print(type(x),type(y))
