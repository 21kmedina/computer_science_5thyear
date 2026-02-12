'''
author:karla patino
date:09/02/2026
importing random exercises
'''

import random 

#ex1
ranNum=random.randit(1,100)
print(ranNum)

#ex2
MyList=['apple','banana','orange','pear','peach']
RandomList=random.choice(MyList)
print(RandomList)

#ex3
a=random.randint(0,1)
b=int(input('Enter 1 for heads and 0 for tails, try to guess the outcome of the toss!'))
if b==a:
    print('YOU WON!!!')
elif b!=a:
    print('YOU LOSE')
    
    
    
