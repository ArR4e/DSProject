import random
import string

def suurväike(x):
    sümbolid = string.punctuation
    juhusliksümbol = random.choice(sümbolid)
    uussõna = ""
    for täht in x:
        if täht in sümbolid:
            uussõna += juhusliksümbol
        elif täht.isupper() == True:
            uussõna += täht.lower()
        elif täht.isupper() == False:
            uussõna += täht.upper()
            
    return uussõna