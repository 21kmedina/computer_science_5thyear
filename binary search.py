'''
Karla Patino
3rd September, Binary Search
'''

lst=[2,5,8,12,16,56,23,72,38,91]
lst.sort()
print(lst)

low=0
high= len(lst)-1
middle= (high+low)//2
value=lst[middle]
print(low, high,middle,value)

while 