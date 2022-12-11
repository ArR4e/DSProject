import string
import random


def suurväike(sõne):
    korrastatud = ''
    kirjavahemärgid = string.punctuation
    for x in sõne:
        if x.isupper():
            uus1=x.lower()
            korrastatud += uus1
        if x.islower():
            uus2=x.upper()
            korrastatud += uus2
        if x == ' ':
            korrastatud += ' '
        if x in kirjavahemärgid:
            korrastatud += x
            
    lõplik = korrastatud
    r = random.choice(kirjavahemärgid)
    
    for x in lõplik:
        if x in kirjavahemärgid:
            lõplik = lõplik.replace(x, r)
    return lõplik
    
    
sõne = input("Sisesta sõne: ")
print(suurväike(sõne))