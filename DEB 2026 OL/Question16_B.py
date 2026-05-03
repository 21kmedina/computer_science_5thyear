# Question 16 B
# 03-05-2026
# Karla Patino
words=input("Enter words:")
space=str(" ")
word=1
vowel=("a","e,i,o,u")
vowels=0
for i in words:
    if i==space:
        word+=1
    if i==vowel:
        vowels+=1
print('Amount of words in sentence :',word,'Vowels in sentence :',vowels)
        