#author:Karla Patino
#date:/2nd october/2025
#description: question 1, while loops excersices
num= 2
total=0
count=0
while num !='':
    num=input('enter a number :')
    if num.isdigit():  
       total+=int(num)
       count+=1
print('avereage is: ',total/count)
