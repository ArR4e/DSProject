import string
from random import randint

def suurväike(sone):
    tyhisone = ''
    margid = string.punctuation
    mark = margid[randint(0,31)]
    for i in sone:
        if i.islower():
            tyhisone += i.upper()
        elif i.isupper():
            tyhisone += i.lower()
        elif i in margid:
            tyhisone += mark
        else:
            tyhisone += ' '
    print(tyhisone)
    return(tyhisone)
margid = string.punctuation
