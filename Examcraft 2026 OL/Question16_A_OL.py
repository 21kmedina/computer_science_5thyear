#Question16_A_OL
#Enter your name here:Karla Patino Medina

print("Welcome to the Step Tracker App!")

name=input("Please enter your name :")

steps_today = int(input("Enter the number of steps you walked today: "))
#this is where the user enters the number of steps


if steps_today <=0:
    print('The number of steps cant be negative')
    
elif steps_today >=10000:
    print("Well done",name,"! You reached your goal.")
    
elif steps_today >=5000 and steps_today<=9999:
    print('Good effort!',name,'Almost there.')
    
elif steps_today<5000:
    print('Try to be more active today',name)
    
