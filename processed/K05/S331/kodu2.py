import string
import random
def suurväike(sõne):
    vahetus = sõne.swapcase()
    märk = random.choice(string.punctuation)
    for char in vahetus:
        if char in string.punctuation:
            vahetus = vahetus.replace(char, märk)
    return vahetus
    