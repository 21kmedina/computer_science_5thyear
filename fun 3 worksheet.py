'''
Karla Patino
date: 15/05/2026
functions 3 worksheet
'''

alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#making a functiuon to encrypt

def encryption():
    last=alpha[-1]
    new=alpha.insert(0,last)
    index=0
    for i in alpha:
        index+=1
        