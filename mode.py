lst=[4,3,2,5,6,3]
#lst=list(input('Enter a list:'))


def range_lst(lst):
    lst.sort()
    range_=max(lst)-min(lst)
    return(range_)
print(range_lst(lst))


u_lst=[]
def mode(lst):
    lst.sort()
    for i in lst:
        if i not in u_lst:
            u_lst.append(i)
            
            
    
    