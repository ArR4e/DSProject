from random import randint
import string
def suurväike(sõne):
    x=0
    märk=string.punctuation[randint(1,len(string.punctuation))]
    uussõne=""
    while x<len(sõne):
        if sõne[x].isupper():
            täht=sõne[x].lower()
        elif sõne[x].islower():
            täht=sõne[x].upper()
        elif sõne[x]==' ':
            täht=" "
        elif sõne[x] in string.punctuation:
            täht=märk
        uussõne+=täht
        x+=1
    return uussõne