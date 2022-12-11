import random
import string
def suurväike(söne):
    uus_sümbol = random.choice(string.punctuation)
    uus_söne = ""
    for i in söne:
        if i in string.punctuation:
            i = uus_sümbol
            uus_söne += i
        else:
            uus_söne += i
            
            
    return(uus_söne.swapcase())


suurväike("Tere, ELISE!%&/()")