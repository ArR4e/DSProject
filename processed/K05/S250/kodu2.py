import random
import string

def suurväike(sõna):
    teis_sõna = ""
    gen_punkt_m = (random.choice(string.punctuation))
    for täht in sõna:
        if (täht.isupper()) == True:
            teis_sõna += (täht.lower())
        elif (täht.islower()) == True:
            teis_sõna += (täht.upper())
        elif (täht.isspace()) == True:
            teis_sõna += täht
        elif täht in string.punctuation:
            
            teis_sõna += gen_punkt_m
    return teis_sõna
    

for i in range(10):
    print(suurväike("kAss!Koer!"))