'''
name:Karla Patino
date:15/12/2025
program:program 1, 5th yr november assessment programing revision 
'''
#STEP 1
winCardnum=('8549018035096133')
print('len of wincard is ,',(len(winCardnum)))

checking_digit=winCardnum[:15]
print('wincard checking digit is,',checking_digit)

lastposition=winCardnum[-1]
print('last position of  the wincard is ,',lastposition)

#STEP 2
reverse=checking_digit[::-1]
print('wincard number reversed is ,',reverse)

#STEP 3 (i)
even_indices=reverse[0::2]
#print(even_indices)
odd_indices=reverse[1::2]
#print(odd_indices)

#(ii)
total_even=0
for i in even_indices:
    i=int(i)
    double=int(2*i)
    
    if double>9:
        double=double-9
    total_even+=double
print('addition of all even numbers ,',total_even)

total_odd=0
for i in odd_indices:
    
    i=int(i)    
    total_odd+=i
print(total_odd)

#STEP 4
total_adition=total_odd+total_even+3
print('the total addition is ,',total_adition)

if total_adition%10==0:
    print('this is a valid card number!!!')
    
else:
    print('this is NOT a valid card number!!!')