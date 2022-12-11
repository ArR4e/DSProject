import string
import random
def suurväike(a):
    b=""
    c=random.choice(string.punctuation)
    for i in a:
        if i in string.punctuation:
            b=b+c
        elif i ==i.upper():
            b=b+i.lower()
        else:
            b=b+i.upper()
        
    return b