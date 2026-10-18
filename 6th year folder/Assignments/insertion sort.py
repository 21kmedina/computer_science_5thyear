''' karla patino
Insertion sort '''

lst=[11,7,14,19,12]
marker=[0]
for x in range(1,len(lst)):
    marker=lst[x]
    for y in range(x-1,-1,-1):
        if lst[y] > marker:
            lst[y],lst[y+1] = lst[y+1], lst[y]
        else:
            break
print(lst)
