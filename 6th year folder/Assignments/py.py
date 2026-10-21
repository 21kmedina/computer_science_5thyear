def frequency_word_or_char(val):
    for word in val:
        if word in dictionary:
            valAdd=dictionary[word]
            valAdd+=1
            dictionary[word]=valAdd
        elif word not in dictionary:
            dictionary[word] = 1
    return(dictionary)

    
dic= {}
lst= []

with open('book.txt','r') as file:
    for line in file:
        words= line.split()
        for i in words:
            if i in dic:
                dic[i]+= 1
            elif i not in dic:
               dic[i]= 1

def sorting(a):
    return a[1]
print(dic)
sorted_words= sorted(dic.items(),key= sorting, reverse=True)[:10]
print(dict(sorted_words))