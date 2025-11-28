'''
Program to encode a value
author:Karla Patino
date:25th-November-2025
unicode to UTF-8

steps,1) ask for unicode, then get first digit or value of the unicode (using string indexing)
step2)convert the first digit/value to hexadecimal.
step3)take leading zeros away for only the first value(if loop), find binary number for the rest of the values
step4)count amount of digits all together and see which row has the same amount of x's for the amount of digits
step 5)write the number in row and fill in the x's space w binary digits
'''


UserInput=input('enter a unicode code to convert to binary :')
i=UserInput[2::]

for x in i:    
    st= ''
    
    if x=='A':
        x=10
    elif:
        x=='B':
         x=11
    elif:
        x=='C':
         x=12
    elif:
        x=='D':
         x=13
    elif:
        x=='E':
         x=14
    elif:
        x=='F':
         x=15
    x=int(x)
    while x>0:
        remainder=x%2
        x=x//2
        if len(remainder)
        st=st+str(remainder)
    print(st[::-1])
        