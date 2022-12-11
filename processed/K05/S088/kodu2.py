from string import punctuation
from random import choice

def suurväike(a):
    if isinstance(a, str):
        b = ""
        p = choice(punctuation)
        for i in a:
            if i.isupper():
                i = i.lower()
            elif i in punctuation:
                i = p
            else:
                i = i.upper()
            b += i
        return b
    else:
        return "Argument peab olema sõne."