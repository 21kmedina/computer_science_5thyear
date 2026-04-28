#Question 16(a)
#Name and School: Karla PAtino , athlone community college
option=int(input('Enter 1 for Celsius to Fahrenheit conversion OR 2 for Fahrenheit to Celsius conversion:'))

if option==1:
    
    celsius=float(input('Enter the temperature in Celsius:'))    
    def celsius_to_fahrenheit(celsius):     
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
    kelvin=celsius+273.15
    print(celsius,"•C is equal to",celsius_to_fahrenheit(celsius),"•F",'and',kelvin,'K' )   
    
elif option==2:# conditional 
    fahrenheit=float(input('Enter the temperature in Fahrenheit:'))
    def fahrenheint_to_celsius(fahrenheint):
        celsius=((fahrenheit - 32)/1.8)       
        return celsius
    
    
    print(fahrenheit,"•F is equal to",fahrenheint_to_celsius(fahrenheit),"•C")