#1
def sum_lst(lst):
    if len(lst)==0:
        return 0
    else:
        return lst[0] + sum_lst(lst[1:])
    
lst=[2,4,5]
print('sum of a list of nums:',sum_lst(lst))

#2
def num_string(string):
    if len(string)==0:
        return 0
    else:
        return 1 + num_string(string[1:])
x='oranges'
print('number of characters in string:',num_string(x))

#3
def sum_d(d):
    if len(d)==0:
        return 0
    else:
        return int(d[0]+ sum_d(d[1:]))
    
digits = [-2,3,-5,5]
print(sum_d(digits))
