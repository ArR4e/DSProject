import string
import random

def suurväike(sone):
    a=random.choice(string.punctuation)
    b= ""
    for i in sone :
        if i in string.punctuation:
            i=a
            b+=i
        else:
            b+=i
        
    return(b.swapcase())
    
