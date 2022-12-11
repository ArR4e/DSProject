import string
import random
def suurväike(sõne):
    sõne=sõne.swapcase()
    
    a=random.choice(string.punctuation)
    for i in range(len(sõne)):
        if sõne[i] in string.punctuation:            
            sõne=sõne.replace(sõne[i],a)
           
    return sõne
    
sõne=input("Kirjuta mingi sõna:")
suurväike(sõne)