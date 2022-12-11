import string
import random
sõne = ".......ASDvcs!Ds%f&gdf"

def suurväike(sõne):
    b = random.choice(string.punctuation)
    ilma = ""
    for i in sõne:
        if i not in string.punctuation:
            ilma = ilma + i
        else:
            ilma = ilma + b
    return ilma.swapcase()

print(suurväike(sõne))
