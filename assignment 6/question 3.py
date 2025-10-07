num=0
while num!='':
    num=input('enter a number :')
    if num.isdigit():
        num=int(num)
        for i in range(0,num):
            if(i%2 == 0):
                print(i)
            
            
    
