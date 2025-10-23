'''
author Karla Patino Medina
23rd october 2025
assignment 10, question 3
'''

word1=input('Enter a word :')
secword=word1[0]
wordthird=word1[1:200]
word4=wordthird.replace(secword,'$')
print(secword+ word4)
