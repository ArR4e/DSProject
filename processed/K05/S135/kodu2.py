from random import choice
import string

def suurväike(sone):
    sone = str(sone)

    sone = sone.swapcase()
    
    # valib suvalise kirjavahemärgi ja asendab iga kirjavahemärgi sõnes sellega
    randKirjavahemark = choice(string.punctuation)
    for char in sone:
        if char in string.punctuation:
            sone = sone.replace(char, randKirjavahemark)
            
    return sone