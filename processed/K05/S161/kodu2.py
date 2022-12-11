import string
import random
tähed=[]
for i in string.punctuation:
    tähed.append(i)
sõna=list("MinA oleN Tubli!!")

def suurväike(sõna):
    sõnauus=[]
    w=random.choice(tähed)
    for rida in sõna:
        if rida.islower():
            x=rida.replace(rida, rida.upper())
            sõnauus.append(x)
        elif rida.isupper():
            y=rida.replace(rida, rida.lower())
            sõnauus.append(y)
        elif rida==" ":
            sõnauus.append(rida)
        else:
            z=rida.replace(rida, w)
            sõnauus.append(z)
    return ''.join(sõnauus)
print(suurväike(sõna))