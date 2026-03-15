'''
Author:Karla Patino
ExamCraft Mock OL (a)
'''
#question 16
#karla patino
 
option= input ("Would you like to (a)dd or (s)ubtract, (m)ultiply or (d)ivide?")
num1=float(input("Please enter your first number :"))
num2=float(input("Please enter your second number :"))
if option == "a":
    total=num1 +num2
    print(num1,"+",num2,"=",round(total,2))
if option == "s":
    total2=num1 - num2
    print(num1,"-",num2,"=",round(total2,2))
if option =="m":
    total3=num1 * num2
    print(num1,"x",num2,"=",round(total3,2))
if option =="d":
    total4=num1/num2
    print(num1,"/",num2,"=",round(total4,2))
