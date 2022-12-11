import string
from random import randint
def suurväike(a):
    b = ""
    märk = string.punctuation[randint(0, len(string.punctuation)-1)]
    for i in a:
        if i in string.punctuation:
            i = märk
        if i.isupper():
            b += i.lower()
        else:
            b += i.upper()
    return(b)
print(suurväike("SeE. on TesTim;iseks"))
