import string
from random import *
import random

def suurväike(sõna):
    sümbol=random.choice(['!','#','%','&','(',')','@','£','$','€','*']) 
    sõna=sõna.swapcase()
    for täht in sõna:
        if täht in string.punctuation:  
           sõna=sõna.replace(täht,sümbol)
                  
    return(sõna)
