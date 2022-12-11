import string
import random
def suurväike(x):
    tagastatav = ""
    a = random.randint(0,31)
    b = string.punctuation
    o = string.punctuation[a]
    for mark in x:
        if mark in b:
            tagastatav += o
        elif x.isspace() == True:
            tagastatav += " "
        elif mark.isupper() == True:
            tagastatav += mark.lower()
        elif mark.isupper() == False:
            tagastatav += mark.upper()
    return(tagastatav)

print(suurväike("MinA oleN Tubli!!"))