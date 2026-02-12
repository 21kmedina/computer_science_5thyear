'''
Author: Karla Patino
About:Import random exercises question 5
'''
import random

q=False
score=0
ans=0
lst=['+','-','*','/']
operation= 0


while q!=True:
    randnum1=random.randint(1,100)  
    randnum2=random.randint(1,100)
    operator = random.choice(lst)
    if operator=='+':
        operation=randnum1+randnum2
    elif operator=='-':
        operation=randnum1-randnum2
    elif operator=='/':
        operation=randnum1//randnum2
    elif operator=='*':
        operation=randnum1*randnum2
    ans=input(f'Calculate {randnum1}{operator}{randnum2} :')
    if ans== 'q':
        break
    ans= int(ans)
    if ans==operation:
        print('This is correct!')
        
        score+=1
        print(score)
        
