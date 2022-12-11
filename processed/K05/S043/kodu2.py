import random
import string
sn = str(input("Sisesta sõne: "))
def suurväike(b):
    f = random.choice(string.punctuation)
    symbolid = string.punctuation
    for symbol in symbolid:
        b = b.replace(symbol, f)
    uus_sone = ""
    uus_sone += b.swapcase() 
    return uus_sone

print(suurväike(sn))