import string
import random
def suurväike(x):
    y = ""
    punc = string.punctuation[random.randint(0, 31)]
    for i in range (len(x)):
        if x[i].isupper():
            y += x[i].lower()
        elif x[i].islower():
            y += x[i].upper()
        elif x[i] in string.punctuation:
            y += punc
        else:
            y += x[i]
    return y