# functions intro,these are part of the course BUT are NOT on the python refernce guide
#use/ call function both ways
some_dict={}
print(some_dict)
#or
some_dict2=dict()
print(some_dict2)

some_dict={'key':'value','fruit':'apple'}
print(some_dict)

#list of tuples
lst_tuples = [('key','value'),('fruit','apple')]

#convert list to dictionary
some_dict2= dict(lst_tuples)
print(some_dict2)
 
#add new item to list
some_dict2['price'] = 2.03
print(some_dict2)

#change fruit to orange
some_dict2['fruit']='orange'
print(some_dict2)
some_dict2['dictionary']= {'a':1,'b':2,'c':3}
print(some_dict2)

#list keys in dictionary
##key jst a variable name
for key in some_dict2.keys():
    print(key)
    
#list values in a dictionary
for values in some_dict2.values():
    print(values)
    
#list keys and values
for key,value in some_dict2.items():
    print(key,'-->',value)
    
#delete item from dictionary
#dictionary name on its onw will delete the entire dictionary
del some_dict2['fruit']
print(some_dict2)

#check if item in dictionary
if 'fruit' in some_dict2:
    print('fruit is still present - failed to delete')
else:
    print('fruit removed')
    
#sort a dictionary by value
new_dict = {'a':5,'b':4,'c':7}
print(new_dict.items())

def sf(x):
    return x[1]#bcs index 1 is position 2
tuple_sorted_dict= sorted(new_dict.items(),key=sf,reverse=True)
print(tuple_sorted_dict)
print(dict(tuple_sorted_dict))
