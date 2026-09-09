#simple sort
lst=[2,5,4]

new_lst=[]

len_lst=len(lst)
val=0

while len_lst > val:
    p1=lst[0]
    p2=lst[1]
    if p1 < p2:
        new_lst.append(p1)
        lst.remove(p1)
        val+=1
        
        print(new_lst,lst)
    
    