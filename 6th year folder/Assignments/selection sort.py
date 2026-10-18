#karla patino , Selection sort, 10th of september 2026

lst=[3,5,2,7,1]
size=len(lst)
min_val=0

for i in range(0,size-1):
    min_val=i
    for j in range(i+1,size):
        if lst[j]<lst[min_val]:
            min_val= j
            lst[i],lst[min_val]=lst[min_val],lst[i]
            
                     
print(lst)
    
