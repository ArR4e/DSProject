import string
from random import *

def suurväike(sõne):
    s = string.punctuation[randint(0,len(string.punctuation))]
    sõne = list(sõne)
    for i in range(len(sõne)):
        if sõne[i].isalpha() == False and sõne[i].isdigit() == False and sõne[i] != " ":
            sõne[i] = s
    return "".join(sõne).swapcase()

print(suurväike("Eh hee"))