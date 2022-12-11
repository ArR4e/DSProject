from random import *
from string import *

def suurväike(str):
    
    str = str.swapcase()
    indeksid = []
    
    for x in punctuation:
        if x in str:
            indeksid.append(punctuation.index(x))
          
    i = randint(0, len(punctuation) - 1)
    
    for x in indeksid:
            
        str = str.replace(punctuation[x], punctuation[i])
    
    return str