import string
import random

def suurväike(allari):
    a = random.choice(string.punctuation)
    for el in allari:
        if el in string.punctuation:
            allari = allari.replace(el, a)
            
    return allari.swapcase()

print(suurväike("MulLe MeEldIB KÄED üLeS TÕSta PLAKSUGA!!#,&"))