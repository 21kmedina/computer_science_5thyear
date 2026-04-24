# Please enter name: Karla Patino

print('************************')
print('       Conversions      ')
print('************************')
print('(1) From teaspoons to ml')
print('(2) From tablespoons to ml')
print('(3) From cups to ml')
print('(4) From ml to teaspoons')
print('(5) From ml to tablespoons')
print('(6) From ml to cups')
conversion= int(input('Enter the conversions, E.g if click on number 3, it will convert cups to ml:'))
if conversion ==1:
    teaspoons=float(input('Please enter the number of teaspoons:'))
    ml=teaspoons*5
    print('The ml is',ml)
elif conversion ==2:
    tablespoons=float(input('Please enter the number of tablespoons:'))
    ml=tablespoons*15
    print('The ml is',ml)
elif conversion==3:
    cups=float(input('Please enter the number of cups:'))
    ml=cups*210
    print('The ml is',ml)
elif conversion==4:
    ml=float(input('Enter amount of ml:'))
    teaspoons=ml/5
    print('The teaspoon is',teaspoons)
elif conversion==5:
    ml=float(input('Enter amount of ml:'))
    tablespoons=ml/15
    print('The tablespoon is',tablespoons)
elif conversion==6:
    ml=float(input('Enter the amount of cups:'))
    cups=ml/210
    print('The cups are',cups)





