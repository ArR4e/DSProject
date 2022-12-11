import string, random

def suurväike(sõne):
    x = random.choice(string.punctuation)
    for i in sõne:
        if i in string.punctuation:
            sõne = sõne.replace(i, x)
    print(sõne.swapcase())
    
x = input()
suurväike(x)