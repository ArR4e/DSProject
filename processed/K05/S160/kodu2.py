#Kodu2.py pole antud hindamiseks, lihtsalt lisapraktikumimaterjal, ei tahtnud tühja kohta
#jätta siia :D 

import string
from random import randrange

uus_mark = string.punctuation[randrange(0, len(string.punctuation))]

def suurväike(symbol):
    if symbol.isalpha():
        print("taht")
        if symbol.isupper():
            print("suurtaht")
            print("vaiketahena oleks", symbol.lower())
        else:
            print("vaiketaht")
            print("suuretahena oleks", symbol.upper())
    elif symbol in string.punctuation:
        print("%")
        return symbol