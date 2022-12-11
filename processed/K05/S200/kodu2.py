import random
import string
def suurväike(a):
    uus = ""
    pikkus = len(a)
    valik = random.choice(string.punctuation)
    for i in a:
        if i.islower() == True:
            i = i.upper()
            uus += i
        elif i.isupper() == True:
            i = i.lower()
            uus += i
        elif i == " ":
            i = " "
            uus += i
        elif i in string.punctuation:
            i = valik
            uus += i
    return(uus)
            