# Karla Patino medina
#30-04-2026
#Intro to functions exercises

#Q2
def animal_crackers(a):
    space=a.find(' ')
    space=space+1 
    return space

a=input('Enter a 2 word string:')
x= animal_crackers(a)
if a[0]==a[x]:
    print('True')
else:
    print('False')