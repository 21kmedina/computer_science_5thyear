'''
author:karla patino
date:12/02/2026
importing random exercises, Coding assignment
program 1- two digit numbers
'''

user_num1=input('Enter a first number with two digits:')
user_num1_reversed=str(user_num1)
user_num1_reversed=user_num1_reversed[::-1]
user_num1_reversed=int(user_num1_reversed)
print(user_num1_reversed)
user_num1=int(user_num1)

user_num2=input('Enter a second number with two digits:')
user_num2_reversed=str(user_num2)
user_num2_reversed=user_num2_reversed[::-1]
user_num2_reversed=int(user_num2_reversed)
print(user_num2_reversed)
user_num2=int(user_num2)

user_num1_squared=user_num1**2
print('The first num enterd squared is:',user_num1_squared)

user_num2_squared=user_num2**2
print('The second num enterd squared is:',user_num2_squared)

user_num1_reversed_squared=user_num1_reversed**2
print('the first reversed squared number is:',user_num1_reversed_squared)

user_num2_reversed_squared=user_num2_reversed**2
print('the second reversed squared num is:',user_num2_reversed_squared)

og_sum=user_num1_squared+user_num2_squared
print('sum of enterd num:',og_sum)
reverse_sum=user_num1_reversed_squared+user_num2_reversed_squared
print('sum of reversed nums:',reverse_sum)

if og_sum==reverse_sum:
    print('answer for both are the same')
elif og_sum!=reverse_sum:
    print('theire answers are not he same')


