import random

def suurväike(sõne):
    l=len(sõne)
    sõna=str()
    märk=random.choice(["!","#","$","%","&","(",")","*","+","-",".",":",";","<","=",">","?","@","[","]","^","{","|","}"])
    for i in range (l):
        if sõne[i].isupper()==True:
            sõna+=(sõne[i].lower())
        elif sõne[i].islower()==True:
            sõna+=(sõne[i].upper())
        elif sõne[i]==" ":
            sõna+=(" ")
        else:
            sõna+=(märk)
    print(sõna)
    return sõna

suurväike("TerE,.,")