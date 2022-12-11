import random, string
def suurväike(b):
    b = b.swapcase()
    c = random.choice(string.punctuation)
    for i in b:
        if i in string.punctuation:
            b = b.replace(i, c)
    return b

