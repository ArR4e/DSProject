b = input("xxxx")
pun = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
from random import*
f = choice(pun)

def suurväike(b):
    b = b.swapcase()
    for i in b:
        if i in pun:
            b = b.replace(i, f)
    return b
         
print(suurväike(b))