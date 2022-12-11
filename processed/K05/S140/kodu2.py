import string
import random

def suurväike(word):
    sõna = ""
    #algne väljundi väärtus on tühi sõne
    märk = random.choice(string.punctuation)
    #märk omistab väärtuseks juhusliku kirjavahemärgi
    for i in word:
        if i == " ":
            sõna += " "
        #kui i on tühik, siis väljundile liidetakse tühik
        elif i.isupper():
            sõna += i.lower()
        #kui i on suur täht, siis ta muudetakse väikseks
        #ja liidetakse väljundile
        elif i.islower():
            sõna += i.upper()
        #kui i on väike täht, siis ta muudetakse suureks
        #ja liidetakse väljundile
        elif i in string.punctuation:
            i = märk
            sõna += i
        #kui i on kirjavahemärk, siis ta muudetakse muutujaks
        #märk ning liidetakse väljundile
    return sõna
