#Question 16(b)
#Karla patino

temperatures=[14,23.5,72,56,45.5]
temp=int(input("Enter a temperature:"))
temperatures.append(temp)
print(temperatures)
len_temp=len(temperatures)
min_val=50000
max_val=-5000
add=0

for i in temperatures:
    if i > max_val:
        max_val = i
    
    if i < min_val:
        min_val = i
        
    if add>=0:
        add+=i
mean=add/len_temp

        
print('Max temperature =',max_val,'Minimum temperature =',min_val,"The mean is:",mean)
        
