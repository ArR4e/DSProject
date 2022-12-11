from random import randint
import string
def suurväike(a):
    sõna = ''
    märk = string.punctuation[randint(0, len(string.punctuation)-1)]
    for i in range(len(a)):
        if a[i] in string.punctuation:
            sõna += märk
        elif a[i].isupper() == True:
            sõna += a[i].lower()
        else:
            sõna += a[i].upper()     
    return sõna   