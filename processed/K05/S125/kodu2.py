from random import *
import string

sõne = input("Sisesta lause/sõna: ")

märgid = string.punctuation #saab kõik märgid

def suurväike(sõne):
    sõne = sõne.swapcase() #vahetab suured/väikesed tähed
    
    #valib juhusliku märgi kõikide märkide hulgast
    number = randint(0, 31)
    märk = märgid[number]
    
    #vahetab kõik sõnes olevad kirjavahemärgid teistsuguse ühe ja sama märgiga
    for i in sõne:
        if i in märgid and i != märk:
            sõne = sõne.replace(i, märk)
            
    return sõne

print(suurväike(sõne))