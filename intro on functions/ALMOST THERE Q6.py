#Question 6, intro to functions.
#ALMOST THERE

def almost_there(num):
    if num >= 90 and num <= 110:
        result=True
    elif num >=190 and num <=220:
        result=True
    else:
        result=False
    return result

num=int(input('Enter an interger :'))
x=almost_there(num)
print(x)