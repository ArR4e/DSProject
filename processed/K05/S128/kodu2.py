#Suured väikeseks ja väikesed suureks
from random import *
import string
def suurväike(sõne):
    sõne_asendatud = ""
    kirjavahemärk = string.punctuation[randint(0,len(string.punctuation))]
    for i in range (len(sõne)):
        if sõne[i].isupper() == True:
            sõne_asendatud += sõne[i].lower()
        elif sõne[i].islower() == True:
            sõne_asendatud += sõne[i].upper()
        elif sõne[i] == " ":
            sõne_asendatud += " "
        else:
            sõne_asendatud += kirjavahemärk
    return sõne_asendatud

sisend_sõne = input("Sisesta mingi sõne: ")
print(suurväike(sisend_sõne))
