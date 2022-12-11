import string
import random

def suurväike(sõne):
    sümbol = random.choice(string.punctuation)
    sümbolid = string.punctuation
    sõne = sõne.swapcase()
    for i in sümbolid:
        sõne = sõne.replace(i, sümbol)
    return(sõne)

# sain siit natuke abi:
# https://www.geeksforgeeks.org/python-remove-punctuation-from-string/