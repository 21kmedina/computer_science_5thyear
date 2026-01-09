'''
name:Karla Patino
date:08/1/2026
program:LISTS, work from the book 11.61A 
'''
#11.61A
lst=[10,12,14]
lst.append(16)
print('11.61A list:',lst)

#11.61B

val=[17,24,15,30]
val.extend([34,27])
print('11.61B list:',val)

#11.4
#eval is a function, NEVER USE IN LC CODE

mylist=[2,4,6]
print('my existing list is:',mylist)
n=eval(input('Enter a number or a list to be appended:'))
if type(n)==type([]):#if a list is input
    mylist.extend(n)
elif type(n)== type(1):#if interger is input
    mylist.append(n)
else:
    print('please enter either an interger or a list.')
print('append list is:',mylist)

#11.6.2
#Inserting an element in a list

val=[17,24,15,30]
val.insert(2,33)  # add number 33 at third position(index 2)
print('11.62 list:',val)

#11.6.3
#modifying/Updating elements to a list

lst=[10,12,14,16]
lst[2]=24 # replace nuumber at index 2, with 24
print('11.63 list:',lst)

#11.6.4A
#deleting an element from a list using its Index /Position
val=[17,24,33,15,30]
deleted_val=val.pop(2)
print('this is the deleted element',deleted_val)
print('11.64.A list:',val)#prints list wihtout the deleted

#11.6.4B
#deleting an element using its value

val=[17,24,33,15,30]#to delete 24, write as follows:
val.remove(24) # deletes 24
print('11.64.B list:',val)

#11.6.4C, deleting a sublist from a list

lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
del lst[10] #deletes num at position 10, so deletes 11
print(lst)