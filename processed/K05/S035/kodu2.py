import string
import random
def suurväike(s):
    uus=random.choice(string.punctuation)
    r=s
    for sümbol in s:
        if sümbol in string.punctuation:
            r=r.replace(sümbol, uus)
    pööratud=""
    pööratud+=r.swapcase()
    return(pööratud)

        