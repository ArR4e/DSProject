import random
import string
sõne = input("Sisesta midagi: ")

def suurväike(sõne):
    #kõik kirjavahemärgid
    märk = string.punctuation
    #valib ühe suvalise märgi
    vahetus = random.choice(märk)
    for i in range (len(sõne)):
        if sõne[i] in märk:
            sõne = sõne.replace(sõne[i], vahetus)
    return(sõne.swapcase())
print(suurväike(sõne))

    