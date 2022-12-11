sõne = "MinA oleN Tubli!!"
from random import randint
import string

def suurväike(sõne):
    rand = randint(1,31)
    punctuation = string.punctuation[rand]
    uussõne = ""
    for i in sõne:
        if i.islower():
            i = i.upper()
            uussõne += i
            
        elif i.isupper():
            i = i.lower()
            uussõne += i
            
        elif i in string.punctuation:
            uussõne += punctuation
            
        elif i == " ":
            uussõne += " "
            
    return uussõne


print(suurväike(sõne))