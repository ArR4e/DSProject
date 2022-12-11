import random

sümbolid = "'!$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'"
def suurväike(sõna):
    tulemus = ""
    for sümbol in sõna:
        if sümbol in sümbolid:
            tulemus += sümbolid[random.randint(0, len(sümbolid)-1)]
        else:
            tulemus += str.swapcase(sümbol)
    return tulemus
        

print(suurväike("t=E.st"))

