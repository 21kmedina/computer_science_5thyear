'''thursday 15th 2026
Karla patino
DICTIONARY intro
'''
def frequency(u):
    lst_words=[]
    frequency_word=0
    word=0    
    for i in u:
        if i not in lst_words:
            lst_words.append(i)
    for k in lst_words:
        frequency_word = u.count(k)
        word=k
        dic[word]=frequency_word
    return(dic)
#Question 1
count=0
sentance=input('Enter a sentance:')
sentance.lower()
word=sentance.split()#for a space it splits word
dic={}
print(sentance)

frequency(word)
for m,n in dic.items():
    print('word -->',m,'|count -->',n)