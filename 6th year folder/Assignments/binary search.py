'''
Karla Patino
3rd of September 2026
Binary Search
'''
lst=[2,5,8,12,16,56,23,72,38,91]
lst.sort()
print(lst)

low=0
high= len(lst)-1
middle= (high+low)//2
value=lst[middle]
print(low, high,middle,value)

if middle==23:
    print(middle,value)
    print(23)
    
elif middle>23:
    high=middle-1 #i put a + instead of a - to get the following value, bcs teams says its middle -1, why?
    if high<low:
        print(-1)
    else:
        middle=(high+low)//2
        
elif middle<23:
    low=middle+1
    if low>high:
        print(-1)
    else:
        middle=(high+low)//2
    


#while value != 23:
    
