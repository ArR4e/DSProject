import string
from random import randrange
o = input("sisesta o: ")
def suurväike(o):
    l = o.swapcase()
    suvaline = string.punctuation[randrange(0, len(string.punctuation))]
    for i in l:
        if not i.isalnum() and i != " ":
            l = l.replace(i, suvaline)
    return(l)
suurväike(o)
