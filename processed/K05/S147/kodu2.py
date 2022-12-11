from string import punctuation
from random import choice
def suurväike(tekst):
    kirjavahemärk = choice(punctuation)
    uussõna = ""
    for täht in tekst:
        if täht.isupper() == True:
            uussõna += täht.lower()
        elif täht.islower() == True:
            uussõna += täht.upper()
        elif täht == " ":
            uussõna += " "
        elif täht in punctuation:
            uussõna += kirjavahemärk
        else:
            uussõna += täht
    return uussõna
print(suurväike(input("Sisestage tekst: ")))