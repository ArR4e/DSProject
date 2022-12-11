import string
import random
def suurväike(a):
    x = ""
    ransym = random.choice(string.punctuation)
    for sym in a:
        if sym.isupper():
            rvs = sym.lower()
            x += rvs
        elif sym.islower():
            rvs = sym.upper()
            x += rvs
        elif sym == " ":
            x += " "
        elif sym in string.punctuation:
            rvs = ransym
            x += rvs
    return x