#11.6.
val=eval(input('Enter a list :'))
print('original list:',val)
val=val*2
print('Replicated list',val)
val.sort()
print('Sorted in acsending order:',val)
val.sort(reverse=True)
print('Sorted in descending order:',val)

#11.7
lst=eval(input('Enter list :'))
length=len(lst)
min_ele=lst[0]
for i in range(1,lenght):
    if lst[i]<min_ele:
        min_ele=lst[i]
        min_index=i
    print('Given list is:',lst)
    print('The minimum element of the given list is:')
    print(min_ele,'at index',min_index)
    
#11.8
lst=eval(input('Enter list:'))
length=len(lst)
mean=sum=0
for i in range(0,length):
    if element == lst[i]:
        print(element,'found at index')
        break
    else:  #
        print(elemet,'not found in given list')
        
#11.11

lst=eval(input('enter list:'))
length=len(lst)
uniq=[]
dupl=[]
count=i=0
while i<length:
    element=lst[i]
    count=1
    f element not in uniq and element not in dupl:
        i+1
        for j in range(i,length):
            if
        
