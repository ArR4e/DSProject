import string
import random
def suurväike(sõne):
    vahetatud_tähed = sõne.swapcase()
    juhuslik_kirjavahemärk = random.choice(string.punctuation)
    for kirjavahemärk in vahetatud_tähed:
        if kirjavahemärk in string.punctuation:
                uus_sõna = vahetatud_tähed.replace(kirjavahemärk, juhuslik_kirjavahemärk)
                return uus_sõna
    else:
        return vahetatud_tähed