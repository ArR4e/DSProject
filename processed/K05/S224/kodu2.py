import string
import random

sõna = input("Sisesta sõne: ")
def suurväike(x):
    y = random.choice(string.punctuation)
    a = string.punctuation
    for symbol in y:
        x = x.replace(a, y)
    uus = ""
    uus += x.swapcase()
    return uus
        
        
print(suurväike(sõna))