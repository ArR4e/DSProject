import string
import re
import random

def suurväike(a):
    a = a.swapcase()
    #võrdub sama asi
    k = string.punctuation
    lst = []
    for i in k:
        lst += [i]
    
    suvaline = random.choice(lst)
    return( re.sub('['+string.punctuation+']',suvaline, a))
"""
temp = ""
    for character in string:
        if character.isupper() == True:
            temp += character.lower()
        else:
            temp += word.upper()
    return temp
"""
    
suurväike("aaa..aaAaa")