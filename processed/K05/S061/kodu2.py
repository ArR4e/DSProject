import string
import random
def suurväike(sõne):
    enõs = ""
    juhuslik = random.choice(string.punctuation)
    for i in string.punctuation:
        sõne = sõne.replace(i, juhuslik)
    for i in sõne:
        if i == i.upper():
            enõs = enõs + i.lower()
        elif i == i.lower():
            enõs = enõs + i.upper()
        elif i == "":
            return enõs
    return enõs
        
print(suurväike(",,Tere minu meelest"))