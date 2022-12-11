import string
import random

def suurväike(a):
    a = str(a)
    m = len(a)
    r = random.randint(0, 31)
    v = ""
    i = 0
    while i < m:
        if a[i].isalpha() == True:
            if a[i].isupper() == True:
                v += a[i].lower()
            else:
                v += a[i].upper()
            i += 1
        elif a[i] == " ":
            v += " "
            i += 1
        else:
            v += string.punctuation[r]
            i += 1
    return(v)