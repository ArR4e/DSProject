import string
import random

def suurväike(sõne):
    muudatus = ""
    märgi_vahetus = random.choice(string.punctuation)
    for i in sõne:
        if i.isupper() or i.islower():
            muudatus += i.swapcase()
        elif i.isspace():
            muudatus += i
        elif i in string.punctuation:
            muudatus += märgi_vahetus
    return muudatus