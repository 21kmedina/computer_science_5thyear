'''
Karla Patino
Dictionary practice

'''
# Question 1
dictionary = {}

def frequency_word_or_char(val):
    for word in val:
        if word in dictionary:
            valAdd=dictionary[word]
            valAdd+=1
            dictionary[word]=valAdd
        elif word not in dictionary:
            dictionary[word] = 1
    return(dictionary)

user_val=input('Enter a sentance :')
user_input=user_val.lower()
word= user_input.split()


User_value=input("Enter 1 to cacluclate the frequency of words OR 2 to count the characters ")
if User_value=="2":
    print("Count of characters -->",frequency_word_or_char(user_input))
elif User_value=='1':
    print("Frequency of words -->",frequency_word_or_char(word))





