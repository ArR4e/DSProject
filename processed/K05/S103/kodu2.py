import random
import string

def suurväike(sõne):
    uus_string = ""
    juhuslik_kirjavahemärk = str(random.choice(string.punctuation))
    for char in sõne:
        if char.isupper() == True:
            uus_string += char.lower()
        elif char in string.punctuation:
            uus_string += juhuslik_kirjavahemärk
        else:
            uus_string += char.upper()
    return uus_string


