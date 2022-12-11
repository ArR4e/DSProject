import string
import random
s = 'minGGI .,.suVaLine tekSt?..'
asendus1 = random.choice(string.punctuation)

def suurväike(s):
    for täht in s:
        if täht in string.punctuation:
            s = s.replace(täht, asendus1)
    print(s.swapcase())
            
suurväike(s)