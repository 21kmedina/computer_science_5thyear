#ask user to enter a string of digits and a step size,add first number
#and all number after, in the step size

UserNum=input('enter a string of numbers:')
UserStep=int(input('enter a step size:'))

addition=0

for num in UserNum[0::UserStep]:
    addition+=int(num)
print(addition)
