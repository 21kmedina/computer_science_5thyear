'''
Name: Karla Patino Medina
Date:5th of November 2025
Assignmnet 12, question 12, questions from the book
'''


formula=input('Enter a sentence with brackets:')
brackets1=formula.count('(')
brackets2=formula.count(')')
print(brackets1+brackets2)
amount=int(brackets1+brackets2)
if amount%2==0:
    print('Theres an even amount of brackerts')
else:
    print('Thres not an even amount of brackets')


