'''
author Karla Patino Medina
24th october 2025
assignment 11, question 2
'''
word=input('Enter a word: ')
word2=word[::-1]
if word2==word:
    print('This is a palindrome')
elif word2!=word:
    print('This is not a palindrome')

    