import string
from random import randint 
def suurväike(tekst):
    uus = ""
    i = randint(0, 31)
    for a in tekst:
        if a.isupper():
            uus += a.lower()
        elif a.islower():
            uus += a.upper()
        elif a.isspace():
            uus += a
        elif a.isdigit() == True:
            uus +=a
            
        elif a.isalpha() == False:
            e = string.punctuation[i]
            uus += e
            
    return uus



    
    
sisend = str(input("Sisesta oma tekst: "))

print(suurväike(sisend))