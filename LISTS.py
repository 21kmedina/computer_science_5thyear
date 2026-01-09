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
print('11.6.4.C list',lst)

#11.5 , asks user to delete or inserting elements in a list.
values=[17,23,18,19]
print('the list is :',values)
while True:
    print('Main Menu')
    print('1.Insert')
    print('2.Delete')
    print('3.Exit')
    choice = int(input('Enter your choice 1/2/3 :'))
    if choice == 1:
        item=int(input('Enter item:'))
        pos=int(input('insert at which position?'))
        index=pos-1
        val.insert(index,item)
        print('Success! list is now:',val)
    elif choice==2:
        print('Delete Menu')
        print('1.Delete using Value')
        print('2.Delete using Index')
        print('3.Delete a sublist')

        dchoice = int(input("Enter choice (1 or 2 or 3): "))
        if dchoice == 1:
            item = int(input("Enter item to be deleted:"))
            val.remove(item)
            print("List now is:", val)

        elif dchoice == 2:
            index = int(input("Enter index of item to be deleted: "))
            val.pop(index)
            print("List now is:", val)

        elif dchoice == 3:
            l = int(input("Enter lower limit of list slice to be deleted:"))
            h = int(input("Enter upper limit of list slice to be deleted:"))
            del val[l:h]
            print("List now is:", val)

        else:
            print("valid choices are 1/2/3 only.")
            
    elif choice == 3:
        break;
    else:

        print("valid choices are 1/2/3 only.")
