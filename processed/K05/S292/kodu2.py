import string
import random

def suurväike(sõne):
    valma = ""
    kirjavahemärgisümbol = string.punctuation[random.randint(0,len(string.punctuation))-1]
    for symbol in sõne:
        if symbol.isalpha() == True:
            if symbol.isupper() == True:
                symbol = symbol.lower()
                valma = valma+symbol
            else:
                symbol = symbol.upper()
                valma = valma+symbol
        elif symbol.isdigit() == True:
            valma = valma+symbol
        else:
            if symbol.isspace() == True:
                valma = valma+" "
            else:
                valma = valma+kirjavahemärgisümbol 
    return valma