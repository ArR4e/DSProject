import string
from random import *

märk = string.punctuation[randrange(0,len(string.punctuation))]
def täht(t):

    if t.isalpha():
        if t.isupper():
            return t.lower()
        elif t.islower():
            return t.upper()
    elif t in string.punctuation:
        return märk
    
def suurväike(s):
    i = 0
    sõne = ''
    while i < len(s):
        
        sümbol = s[i]
        uustäht = täht(sümbol)
        sõne += uustäht
        i +=1
    return sõne