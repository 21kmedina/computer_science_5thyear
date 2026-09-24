'''
Karla Patino medina
24/09/2026
functions
'''
#user_input=eval(input('Enter a list of numbers'))
lst=[4,3,2,5,6]
def mean(lst):
    add=sum(lst)
    mean_l=add//len(lst)
    return mean_l
print(mean(lst))

def median(x):
    lst.sort()
    if len(lst)%2==0:
        x=((len(lst)//2)+((len(lst)//2)+1))//2
        
    else:
        #index=int(len(lst)//2)
        #med=sort_l[index]
        x=len(lst)//2
    med=lst[x]
    return(med)
print(median(lst))    