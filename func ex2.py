#Functions excercise 2

#Part 1
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
a=average(result)
print('Average is :',a)

#Part 3

def median(b):
    lst=sorted(lst)
    if len(lst)%2==1:
        med_lst=len(lst)/2
        indx=int(round(med_lst,1))
        result=lst[indx]

    elif len(lst)%2==0:
        lst=sorted(lst)
        med_lst=len(lst)/2
        indx=int(round(med_lst,1))
        med_lst=(lst[indx]+lst[indx-1])
        med_lst=med_lst/2
        result=med_lst
    return result

b = median(lst)
print('Median value :',b)


#Part 4
def mode_val(lst):
    for i in lst:
        count=lst.count(i)
        if count > 1 :
            mode=i
            break
        else:
            mode='Nothing'           
    return mode

c=mode_val(lst)
print('The mode value is :',c)
