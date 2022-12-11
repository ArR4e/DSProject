import string
from random import randrange

def suurväike(x):
    new_str=""
    uus_märk = string.punctuation[randrange(0, len(string.punctuation))]
    for i in range (len(x)):
        if x[i].isupper():
            new_str+=x[i].lower()
        elif x[i].islower():
            new_str+=x[i].upper()
        elif x[i] in string.punctuation:
            new_str+=uus_märk
    return(new_str)