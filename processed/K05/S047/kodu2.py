import string
from random import*
def suurväike(sõne):
    b=randint(0,len(string.punctuation)-1)
    asendus=string.punctuation[b]
    a=""
    for i in sõne:
        if i.islower():
            a=a+i.upper()    
        elif i.isupper():
            a=a+i.lower()
        elif i in string.punctuation:
            a=a+asendus
        elif i == " ":
            a=a+" "
    return a    

print(suurväike("aaP:tere * Jou"))

