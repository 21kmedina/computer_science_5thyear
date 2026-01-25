'''
name:Karla Patino
date:25th-Jan-2026
code:list exercises,question 9
'''

lst=eval(input('Enter a list :'))

lst2=[]
last_dig=lst[-1]

lst2.append(last_dig)
index=1
last_position=len(lst)-1

for charInposition in lst:
    lst2.append(charInposition)
    index+=1
    if index > last_position:
        break    

print(lst2)
    
    
    
