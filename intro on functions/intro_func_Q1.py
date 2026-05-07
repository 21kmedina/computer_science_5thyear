# Karla Patino medina
#30-04-2026
#Intro to functions exercises

#Q1

def even_or_odd(a,b):
    if (a%2==0) and (b%2==0):
        if a<b:
            result=a
        elif b<a:
            result=b
    else:
        if a>b:
            result=a
        elif b>a:
            result=b
    return (result)
x= even_or_odd(9,7)
print(x)
