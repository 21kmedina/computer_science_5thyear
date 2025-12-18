'''
name:Karla Patino
date:18/12/2025
program:program 2, 5th yr november assessment programing revision 
'''
winCard=('8549018035096133')
#step 1
last_dig=winCard[-1]
print('the last digit is ',last_dig)

checking_digit=winCard[:15]
print('wincard checking digit is,',checking_digit)
#step 2

reverse=' '
for i in checking_digit:
    reverse=i+reverse
print('reversed is,',reverse)
#step 3

even=''
for i in range(0,15,2):
    
    even+=reverse[i]
print(even)

odd=''
for i in range(1,15,2):
    
    odd+=reverse[i]
print('odd nums,',odd)

total_even=0
for i in even:
    i=int(i)
    double=int(2*i)
    
    if double>9:
        double=double-9
    total_even+=double
print('addition of all even numbers ,',total_even)

total_odd=0
for i in odd:
    
    i=int(i)    
    total_odd+=i
print(total_odd)

total_adition=total_odd+total_even+3
print('the total addition is ,',total_adition)

if total_adition%10==0:
    print('this is a valid card number!!!')
    
else:
    print('this is not a valid card number!!!')
