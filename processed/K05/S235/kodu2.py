import random
import string
def suurväike(sõne):
    uus_sõne = ''
    kirjavahemärgid = random.choice(string.punctuation)
    
    for char in sõne:
        if char == ' ':
            uus_sõne += ' '
        elif char in string.punctuation:
            uus_sõne += kirjavahemärgid
        elif char.islower() == True:
            vahetus1 = char.swapcase()
            uus_sõne += vahetus1
        elif char.isupper() == True:
            vahetus2 = char.swapcase()
            uus_sõne += vahetus2
    return uus_sõne