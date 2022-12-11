import string
from random import randint

def suurväike(tekst):
    symbolid = string.punctuation
    symbol = symbolid[randint(1, len(symbolid))]
    uustekst = ""
    for i in tekst:
        if i.isnumeric():
            uustekst += i
        elif i.isalpha():
            uustekst += i.swapcase()
        elif i == " ":
            uustekst += i
        else:
            uustekst += symbol
    return uustekst


    
    
