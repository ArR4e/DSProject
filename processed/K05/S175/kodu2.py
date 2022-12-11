import string
import random
def suurväike(sõna):
    märgid = string.punctuation
    suvaline = random.choice(string.punctuation)
    for i in sõna:
        if i in märgid:
            sõna = sõna.replace(i, suvaline)
    if not sõna.islower() and not sõna.isupper():
        return sõna.swapcase()
    
    


       
                 
        
    
        
   

    