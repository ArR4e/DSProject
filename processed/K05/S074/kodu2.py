#Impordin vajalikud moodulid
import string
import random
#Sisestan lasue mida soovin muuta
sv = input("Sisesta siia lause mida soovid muuta: ")
#Annan sõnele "märgid" väärtuse string.punctuation
märgid = string.punctuation
#Defineerin funktsiooni, mis muudab suured tähed väikesteks ja vastupidi
def suurväike(sv):
    random_symbol = random.choice(märgid)
    muudetud_lause = sv.swapcase()
#Kasutan foor loopi, mis otsib sisestaud lausest kirjavahemärke ja vahetab need juhuslike vastu
    for i in märgid:
        muudetud_lause = muudetud_lause.replace(i , random_symbol)
    return muudetud_lause
#Annan muudetud lausele uue väärtuse
muudetud_lause = suurväike(sv)
#Väljastan ümber tehtud lause
print(muudetud_lause)