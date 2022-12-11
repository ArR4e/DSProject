import string
import random
def suurväike(sõne):
    e=""
    v=random.choice(string.punctuation)
    for i in sõne:
        if i.islower():
            i=i.upper()
            e+=i
            continue
        elif i.isupper():
            i=i.lower()
            e+=i
            continue
        elif i in string.punctuation:
            i=i.replace(i, v)
            e+=i
            continue
        elif i ==" ":
            e+=i
            continue
        else:
            continue
    return e
