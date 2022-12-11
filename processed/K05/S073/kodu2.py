import string
import random

def suurväike(x):
    newstring = ""
    p = random.choices(list(string.punctuation))[0]
    for i in x:
        if i in string.punctuation:
            newstring+=p
        else:
            if i.islower():
                newstring += i.upper()
            else:
                newstring += i.lower()

    return newstring