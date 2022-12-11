from random import *
import string
sõne = input("palun sisestage sõne: ")

x = []
x = string.punctuation
nihe = randint(1, 30)
pikkus = (len(x)-1)
def suurväike(sõne):
    vastus = ""
    for i in sõne:
        if (i in x):
            nr  = x.index(i) + nihe
            if nr > pikkus:
                nr = nr - pikkus
            vastus += x[nr]
            
        elif i.islower():
            a = i.upper()
            vastus += a
        elif i.isupper():
            a = i.lower()
            vastus += a
        elif i == " ":
            vastus += " "
    return vastus
print(suurväike(sõne))
