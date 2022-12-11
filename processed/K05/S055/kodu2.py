from string import punctuation
from random import choice

def suurväike(str):
    m2rk = choice(punctuation)
    swap = str.swapcase()
    for i in swap:
        if i in punctuation:
            swap = swap.replace(i,m2rk)
    return swap
