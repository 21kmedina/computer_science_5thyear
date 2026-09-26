'''
Karla Patino
2nd of September 2026
Linear search
'''
lst=eval(input('enter a list:'))
find=int(input("Enter value you want to find:"))

for i in lst:
    if find == i:
        index=int(lst.index(find))
        print("the index of the value is",index)
        
    elif find not in lst:
        print('-1')
        break
