import string
from random import *

def suurväike(a):
    uussone=""
    randsymb = choice(string.punctuation)
    for sone in a:
        if sone == " ":
            uussone += " "
        if sone.isalnum() == True:
            if sone.isupper() == True:
                uussone += sone.lower()
            else:
                uussone += sone.upper()
        else:
            if sone in string.punctuation:
                uussone += randsymb

    return uussone

print(suurväike("O!. abiTs"))



