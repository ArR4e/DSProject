import string
from random import randrange

def suurväike(sõne):
    i = 0
    for i in sõne:
        if i.isalpha():
            if i.isupper():
                i = i.lower()
            else:
                i = i.upper()
        elif i in string.punctuation:
            i = string.punctuation[randrange (0, len(string.punctuation))]
            i += 1

print(suurväike("TeRe"))
            