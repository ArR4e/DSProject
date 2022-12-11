import random

def suurväike(x):
    symbol = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    symbol1 = symbol[random.randint(0,len(symbol))]
    y = x.swapcase()
    z = ''
    for i in range(0,len(y)):
        if y[i] in symbol:
            z += symbol1
        else:
            z += y[i]
    return z