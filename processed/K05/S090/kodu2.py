import string
import random
def suurväike(x):
    s=""
    a = random.choice(string.punctuation)
    for i in x:
        if i == i.upper() and not i in string.punctuation:
            s += i.replace(i, i.lower())
        if i == i.lower() and not i in string.punctuation and not i == " ":
            s+= i.replace(i, i.upper())
        if i in string.punctuation:
            s+= i.replace(i, a)
    return s
