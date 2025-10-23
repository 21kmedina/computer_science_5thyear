'''
author Karla Patino Medina
23rd october 2025
assignment 11, question 1(ii)
'''

lenght = 0
while lenght!='':
    word=input('Enter a word :')
    if word.isalpha():
        lenght=len(word)
    print(word[-1::-1])
    