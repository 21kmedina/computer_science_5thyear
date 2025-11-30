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
userInput=input('enter a unicode code to convert to binary : ')
userInputHexPart=userInput[2::]

decimalValue=0
finalBinaryValue=''
for characterInTurn in userInputHexPart:
    st= ''
    if characterInTurn=='A':
        decimalValue=10
    elif characterInTurn=='B':
        decimalValue=11
    elif characterInTurn=='C':
        decimalValue=12
    elif characterInTurn=='D':
        decimalValue=13
    elif characterInTurn=='E':
        decimalValue=14
    elif characterInTurn=='F':
        decimalValue=15
    else:
        decimalValue=int(characterInTurn)
       
    ' Convert binary '
    binaryNum=''

    while decimalValue > 0:
        if decimalValue%2==0:
            binaryNum='0' + binaryNum
        else:
            binaryNum='1' + binaryNum
        decimalValue=decimalValue//2

    if len(binaryNum) == 0:
        binaryNum='0000'
    elif len(binaryNum) == 1:
        binaryNum='000' + binaryNum
    elif len(binaryNum) == 2:
        binaryNum='00' + binaryNum
    elif len(binaryNum) == 3:
        binaryNum='0' + binaryNum

    print ('binaryNum: ', binaryNum)
    finalBinaryValue=finalBinaryValue+binaryNum
print('finalBinaryValue', finalBinaryValue)

lengthOfFinalBinaryValue=len(finalBinaryValue)

if lengthOfFinalBinaryValue<=7:
    spacesRemaindingInByte=7-lengthOfFinalBinaryValue
    zeroPad=''
    while spacesRemaindingInByte>0:
        zeroPad+='0'
        spacesRemaindingInByte=spacesRemaindingInByte-1
    print('UTF format ->','0'+zeroPad+finalBinaryValue)
