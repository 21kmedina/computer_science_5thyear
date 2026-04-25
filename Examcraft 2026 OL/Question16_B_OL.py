#Question_16_B_OL
#Enter your name here: Karla Patino

print('Welcome to my weekly step tracker!')

mon=int(input('Enter the number of steps you did on Monday:'))

tue=int(input('Enter the number of steps you did on Tuesday:'))

wed=int(input('Enter the number of steps you did on Wednesday:'))

thurs=int(input('Enter the number of steps you did on Thursday:'))

fri=int(input('Enter the number of steps you did on Friday:'))

sat=int(input('Enter the number of steps you did on Saturday:'))

sun=int(input('Enter the number of steps you did on Sunday:'))

weekly_steps=[mon,tue,wed,thurs,fri,sat,sun]
print('The list of steps is:',weekly_steps)
weekly_total=int(mon+tue+wed+thurs+fri+sat+sun)
print('The total steps taken this week was:',weekly_total)

avg_daily_steps=int(mon+tue+wed+thurs+fri+sat+sun)/7
print('The avg number of steps is:',avg_daily_steps)
#unsure how to only get last 2 dec rounded

for i in weekly_steps:
    if i > weekly_steps:
        print('The largest number of steps is:',i)
    elif i<weekly_steps:
        i=weekly_steps
