# Question 16(a)
# Examination Number:Karla Patino Medina
# 10-10-2026

# function definition used in part (v)
def is_anagram(w1, w2):
    if sorted(w1.upper()) == sorted(w2.upper()):
        return True
    else:
        return False

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
# test whether the sorted strings are the same as each other
# if the sorted strings are the same then they must be anagrams
if (sorted(word1.upper()) == sorted(word2.upper())):
    print(word1,"is an anagram of",word2)
elif (sorted(word1.upper()) != sorted(word2.upper())):
    print(word1,"is NOT an anagram of",word2)
    
if is_anagram(word1,word2) == True:
    print(word1,"is an anagram of",word2)
else:
    print(word1,"is NOT an anagram of",word2)
    
# anagram of a phrase    
p_space= input("Enter a phrase:")

phrase=p_space.replace(" ","")
phrase_lst=[]
    
if (sorted(word1.upper())) == sorted(phrase.upper()):
    print(word1,'is an anagram of',phrase)
    
elif (sorted(word1.upper())) != sorted(phrase.upper()):
    print(word1,'is NOT an anagram of',phrase)
    
if sorted(word2.upper()) == sorted(phrase.upper()):
    print(word2,'is an anagram of',phrase)
    
elif sorted(word2.upper()) != sorted(phrase.upper()):
    print(word2,'is NOT an anagram of',phrase)



    

