import string
from random import randint

def suurväike(tekst):
    p=string.punctuation
    juhuslik=p[randint(0,len(p)-1)]
    t=tekst.swapcase()
    for i in range(len(t)):
        if t[i].isalnum()==False and t[i]!=" ":
            t=t.replace(t[i],juhuslik)
    return t