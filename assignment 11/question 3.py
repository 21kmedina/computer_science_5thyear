'''
author: Karla Patino medina
date: 3rd november 2025
assignment 11 queston 3
'''
total = 0
word=input('Enter a word:')
for letter in word:
    if letter.isdigit():
        total=total+int(letter)
print(total)
        
        