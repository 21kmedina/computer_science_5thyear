#karla patino
#1-5-2026,  Functions q3

#Makes TWENTY

def twenty(a,b):
    if a+b==20 or a==20 or b==20:
        result=('True')
    else:
        result=('False')    
    return result


a=int(input('Enter values for a:'))
b=int(input('Enter values for b:'))

x=twenty(a,b)

print(x)
    