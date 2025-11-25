'''
Program to encode a value
author:Karla Patino
date:25th-November-2025

steps,1) ask for unicode, then get first digit or value of the unicode (using string indexing)
step2)convert the first digit/value to hexadecimal.
step3)take leading zeros away for only the first value(if loop), find binary number for the rest of the values
step4)count amount of digits all together and see which row has the same amount of x's for the amount of digits
step 5)write the number in row and fill in the x's space w binary digits
'''


UserInput=input('enter a unicode code to convert to binary :')
UniCode=int(UserInput)
firstValue=Unicode[0]
firstValue  # convert hex to decimal 
x=x(len[2:])# do not count u+, start hexo to decimal in second postion 