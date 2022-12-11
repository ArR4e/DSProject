import string
import random
def suurväike(sõne):
    sõne = list(sõne)
    i = -1
    for tähis in sõne:
        i += 1
        if tähis == (' '):
            sõne[i]= ' '
        elif tähis.isupper():
            sõne[i]=tähis.lower()
        elif tähis.islower():
            sõne[i]=tähis.upper()
        else:
            märgid = list(string.punctuation)
            sõne[i]=random.choice(märgid)
            
            
    sõne = ''.join(sõne)       
    return sõne
    

    