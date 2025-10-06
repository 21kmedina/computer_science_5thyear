#author:Karla Patino
#date:/06 october/2025
#description: question 2, 

grade=2
total=0
count=0

while grade!='':
    grade=input('enter you grade :')
    if grade.isdigit():
        grade=int(grade)
        total=total+grade
        count+=1
        avg=total/count
print(avg)

if(avg >=90):
    print('You got an A ')
    
elif(avg>80) and (avg<90):
    print('your grade is B')
    
elif(avg>70)and(avg<89):
    print('your grade is C')
    
elif(avg>60)and(avg<79):
    print('your grade is D')
    
else:
    print('Your grade is F')

