def sum_lst(lst):
    if len(lst)==0:
        return 0
    else:
        return lst[0] + sum_lst(lst[1:])
    
lst=[2,4,5]
print(sum_lst(lst))