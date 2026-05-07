lst=eval(input('Enter a number of intergers :'))
lst=list(lst)
print(lst)

result=0
def range_value(x):
    result=max(lst)- min(lst)
    return result

x=range_value(result)
print('range value is :',x)

#Part 2
avg=0
def average(a):
    avg=sum(lst)/len(lst)
    return avg
a=average(avg)
print('Average is :',a)

#Part 3
med_lst=0
def median(b):
     lst=sorted(lst)
    if len(lst)%2==1:
        med_lst=len(lst)/2
        indx=int(round(med_lst,1))
        result=lst[indx]
        
    elif len(lst)%2==0:
        med_lst=len(lst)/2
        result=med_lst
    return result

b = median(result)
print('Median value :',b)
