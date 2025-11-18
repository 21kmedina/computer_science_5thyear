'''
Author:Karla Patino 
Date:18th Nov 2025
Programm: addition of two binary numbers 
'''

User_binary1=input('Enter 1st binary number: ')
User_binary2=input('Enter 2nd binary number: ')

addition=0
carryOn=0
reminder=0
result=''
binaryOneLen=len(User_binary1)

for position in range(binaryOneLen,0,-1):
    valueInPosition1=int(User_binary1[position-1])
    valueInPosition2=int(User_binary2[position-1])

    if (valueInPosition1==1 or valueInPosition1==0) and (valueInPosition2==0 or valueInPosition2==1):
        addition=valueInPosition1+valueInPosition2+carryOn
        if addition>=2:
            carryOn=1
            reminder=addition-2
        else:
            carryOn=0
            reminder=addition
        result=str(reminder)+result
    else:
        print ('Invalid numbers: ', valueInPosition1, valueInPosition2)
        break;
print ('Result: ', int(str(carryOn) + result))   
