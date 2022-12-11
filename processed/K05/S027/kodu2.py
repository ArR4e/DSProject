import string
from random import randrange

def suurväike(x):
    sümbol = list(string.punctuation)
    a = randrange(0, 31)
    b = 0
    x = list(x)

    for i in x:
        if i in string.punctuation:
            x[b] = sümbol[a]
        elif i == i.upper():
            x[b] = i.lower()
        elif i == i.lower():
            x[b] = i.upper()
        b += 1
    x = ''.join(x)
    return x