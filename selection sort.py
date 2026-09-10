#karla patino , Selection sort, 10th of september 2026

lst=[3,5,2,7,1]
size=len(lst)
marker=1

for i in range(0,size-1):
    if lst[i] >lst[marker]:
        lst[i],lst[marker]=lst[marker],lst[i]
        marker+=1
    elif lst[i] < lst[marker]:
        marker+=1
                     
print(lst)
    