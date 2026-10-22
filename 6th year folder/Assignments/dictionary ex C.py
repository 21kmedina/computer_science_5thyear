#Question 16 (a)
# Karla Patino
 
# Function to calculate readability score of text
def calculate_readability_score (text):
    # Split the text into a list of words
    words = text.split()
    print("The list of words in the text is:\n", words)
 
    # Initialise the word counters
    word_count = len (words) # Number of words in list
    short_word_count = 0
       
    for i in words:
        if len(i) <= 2:
            short_word_count += 1
 
    # Initialise the number of sentences
    sentence_count = text.count(".")
    sentance_count2 = text.count('!')
    
    # Calculate the readability score
    score = word_count * (sentence_count + sentance_count2)
    
    div1=word_count/(sentence_count + sentance_count2)
    div2=(word_count - short_word_count)/word_count
    mult1=100 * div2
    add1=div1+mult1
    tot_formula=0.4 * add1
    
    print('Short words:',short_word_count)
    score = round (tot_formula,2) # Round the score to 2 d.p.
    return score

# Set the text for analysis
text1 = "Elaborate sentences influence readability in subtle and unpredictable ways."
text2 = "I do not like green eggs and ham! I do not like them Sam I am!"
 
# Calculate the score for text1
score1 = calculate_readability_score(text1)
print(f'Readability Score 1: {score1} \n')
 
# Calculate the score for text2
score2 = calculate_readability_score(text2)
print(f'Readability Score 2: {score2} \n')

if score1 == score2:
    print("Both scores are the same.")
elif score1 < score2:
    print("The first text is easier to read.")
elif score2<score1:
    print("The second text is easier to read.")
    
    
