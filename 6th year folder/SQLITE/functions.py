'''
Functions
25th september
Karla Patino'''

user_lst=[2,5,4,1,1,1]
# user_lst = input('Type lst here: ')
# user_lst = list(user_lst)

# mean
def mean_of_lst(a):
    total_sum=0
    for i in user_lst:
        total_sum+=i
    mean=total_sum/len(user_lst)
    return(mean)
print('Mean of list is :',mean_of_lst(user_lst))

def median_of_lst(a):
    user_lst.sort()
    if len(user_lst)%2 == 0:
        idx2=len(user_lst)//2
        pos2=user_lst[idx2]
        idx1=idx2-1
        pos1=user_lst[idx1]
        median=(pos1+pos2)/2
        return(median)
    elif len(user_lst)%2 != 0:
        median_idx=(len(user_lst)-1)//2
        median=user_lst[median_idx]
        return(median)
print("Median of list is :",median_of_lst(user_lst))


def mode_of_lst(a):
#      unique_lst=[]
#      mode_lst=[]
#      for i in user_lst:
#          if user_lst.count(i)<2:
#              unique_lst.append(i)
#          elif user_lst.count(i)>2:
#              mode_lst.append(i)
    frequency = []
    for i in user_lst:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    return(frequency)
    print("Frequency of each number:", frequency)           
print(mode_of_lst(user_lst))

def range_of_lst(a):
    user_lst.sort
    range_lst=max(user_lst)-min(user_lst)
    return(range_lst)
print('Range of list is :',range_of_lst(user_lst))


        
