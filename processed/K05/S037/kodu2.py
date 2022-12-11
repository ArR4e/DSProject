import string
import random

def suurväike(sõne):
    lause = ""
    märk = random.choice(string.punctuation)
    for sümbol in sõne:
        if sümbol.isupper():
            sümbol = sümbol.lower()
            lause += sümbol
        elif sümbol.islower():
            sümbol = sümbol.upper()
            lause += sümbol
        elif sümbol == " ":
            sümbol = " "
            lause += sümbol
        else:
            lause += märk
    return lause   
    
    
        