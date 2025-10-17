'''authour karla
assignmnet 9 question 3
17th of october 2025
modify word based on place of vowels'''

word=input('Enter a word :')
if(word[0]=='a'or word[0]== 'e'or word[0]== 'i'or word[0]== 'o'or word[0]== 'u'or word[0]== 'A'or word[0]== 'E'or word[0]== 'I'or word[0]== 'O'or word[0]== 'U'):
    print(word+'way')

else:
    newword=''
    for i in range(1,len(word)):
        newword=newword+word[i]
    newword=newword+word[0]
    print(newword+'ay')

