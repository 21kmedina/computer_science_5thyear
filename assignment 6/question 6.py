'''
Karla Patino Medina
9th October 2025
assignment 6, qsnt 6
take numbers until the total of all numbers is greater then 50

'''
num=0
total=0
while num < 50:
     num=int(input('Enter a number :'))
     total+=num
     if total>=50:
         break
print(total)
     