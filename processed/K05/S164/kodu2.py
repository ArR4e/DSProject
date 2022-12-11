# import string
# 
# sõne = input("Sisesta sõne: ")
# def suurväike(sõne):
#     print(str.swapcase(sõne))
#     
# suurväike(sõne)

import string
from random import randrange
sisend_sõne = input("Sisestage sõne: ")

def suurväike(sõne):
    sõne_pikkus = len(sõne)-1
    asukoht = 0
    väljund_sõna = ""
    while sõne_pikkus >= asukoht:
        sümbol = sõne[asukoht]
        suvaline_sõne = string.punctuation[randrange(0, len(string.punctuation))]
        if sümbol.isalpha():
            sümbol = str.swapcase(sümbol)
        else:
            sümbol = suvaline_sõne
            
        väljund_sõna = väljund_sõna + sümbol
        asukoht += 1
        
    print(väljund_sõna)
    
suurväike(sisend_sõne)
        
    
    
#     elif sõne in string.punctuation:
#     print(uus_sõne)