'''
Author:Karla Patino
ExamCraft Mock OL (b)
'''
#Q 16
#karla patino
 
import random
words = ["Cat","Mat","Can","Man","Pool","Tool","Mule","Pat","Tan","Rule"]
print("The list of words is :", words)
random_word=words[random.randint(0,len(words)-1)]
print("The length of the word is :",len(random_word))
print("The first letter of the word is :",random_word[0])

turns=0

while turns<3:
    guess=input("Please guess the word :")
    if guess==random_word:
        print("You guessed correctly!")
        break
    elif guess != random_word:
        print("Incorrect guess, try again")
        turns+=1
        if turns==3:         
            print("The correct word was",random_word)
            
        
        
        
        
        