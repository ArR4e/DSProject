import random
suvaline = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
def suurväike(sõne):
    muudetud = ""
    a = random.choice(suvaline)
    for täht in sõne:
        if täht.isupper() == True:
            täht = täht.lower()
        elif täht.islower() == True:
            täht = täht.upper()
        elif täht == " ":
            täht = " "
        else:
            täht = a
        muudetud += täht
    return muudetud

print(suurväike("MinA oleN Tubli!!"))    