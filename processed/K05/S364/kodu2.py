import string
from random import*

def suurväike(x):
    newword = ""
    dlina = len(string.punctuation)
    cifra = randint(1, dlina-1)
    symbol = string.punctuation[cifra]
    for i in x:
        if i.isupper():
            i = i.lower()
            newword += i
        elif i.islower():
            i = i.upper()
            newword += i
        elif i == " ":
            newword += i
        else :
            i = symbol
            newword += i
    return(newword)

print(suurväike("AbCdEfGhIjKlMnOpQrStUvWxYz"))
    
    
    
    
    
    
    
