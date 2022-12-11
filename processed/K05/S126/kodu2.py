#importimine
import string
import random

#programmi päis
def suurväike(x):
    kirjavahemärk = random.choice(string.punctuation)
    for mark in string.punctuation:
        x = x.replace(mark, kirjavahemärk)
        
    print(x.swapcase())
    