import string
import random

def suurväike(a):
    a = a.swapcase()
    b = str.maketrans(string.punctuation, random.choice(string.punctuation)*32)
    c = a.translate(b)
    return c