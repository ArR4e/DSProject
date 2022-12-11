import string
import random
import re

def suurväike(sõne):
    muudetud = ""
    muudetud += sõne.swapcase()
    vastus = re.sub("["+string.punctuation+"]",random.choice(string.punctuation),muudetud)
    return vastus
    