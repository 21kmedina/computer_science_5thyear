'''
name:karla patino
date:11th-dec-2025
code:question 5,revision assignmenet1
'''
user_input=int(input('Enter a number :'))
len_user_input=int(user_input+1)

product=1
for i in range(1,len_user_input):
    if i%2:
        even_num=i%2
        even_num = even_num + 1
        print(even_num)
    else :
        product=product+1
    print(product)
        