#simple sort,karla patino 10th of september#
lst=[2,5,4]

new_lst=[]

len_lst=len(lst) +1
val=len_lst

while len_lst >= val:
    len_lst-=1
    if len_lst>1:
        p1=lst[0]
        p2=lst[1]
        if p1 < p2:
            new_lst.append(p1)
            lst.remove(p1)
            val-=1
        elif p2 < p1:
            new_lst.append(p2)
            lst.remove(p2)
            val-=1
    else:
          new_lst.append(p1)
          lst.remove(p1)
print(new_lst,lst)
    
    
