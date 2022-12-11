# 1. Teksti analüüs
# Kirjuta funktsioon erinevad_sümbolid, mis võtab argumendiks sõne ning tagastab kõigi antud sõnes leiduvate erinevate sümbolite hulga.

# >>> erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente")
# {'h', 'e', 'r', 'v', 'l', 'k', 'i', 'g', 't', 'd', 's', 'u', 'a', ' ', 'm', 'o', 'n'}

# Seejärel kirjuta funktsioon sümbolite_sagedus, mis võtab argumendiks sõne ja tagastab sõnastiku,
# mille kirjeteks on sõnes sisalduvad tähed koos nende esinemissagedustega. Sõnastiku võtmeteks peaksid olema
# tähed või muud sümbolid (st tehniliselt võttes sõned) ja väärtusteks täisarvud.

# >>> sümbolite_sagedus("Hei hopsti, väikevend!")
# {'H': 1, 'e': 3, 'i': 3, ' ': 2, 'h': 1, 'o': 1, 'p': 1, 's': 1, 't': 1, ',': 1, 'v': 2, 'ä': 1, 'k': 1, 'n': 1, 'd': 1, '!': 1}

# Loo funktsioon grupeeri, mis võtab argumendiks sõne ja tagastab sõnastiku, kus on kolm võtit: täishäälikud,
# kaashäälikud ja muud sümbolid (st kirjavahemärgid ja tühikud). Iga võtme väärtuseks on vastavat tüüpi häälikute ning
# esinemissageduste paaride hulk.

# >>> grupeeri("sõida tasa üle silla")
# {'Täishäälikud': {('a', 4), ('e', 1), ('i', 2), ('õ', 1), ('ü', 1)}, 'Kaashäälikud': {('d', 1), ('l', 3), ('t', 1), ('s', 3)}, 'Muud': {(' ', 3)}}

# Automaatkontroll. Igal funktsioonil on üks sõnetüüpi parameeter. Esimene funktsioon tagastab hulga, ülejäänud kaks sõnastiku. Kolmanda funktsiooni sõnastikus on iga võtme väärtuseks hulk; paarides on esimene element sõne, teine täisarv. Suur- ja väiketähed loetakse igal pool erinevaks. Piisab esitada ainult funktsioonide definitsioonid.


def erinevad_sümbolid(sõne):
    return set(sõne)

def sümbolite_sagedus(sõne):
    d = {}
    for sümbol in sõne:
        d[sümbol] = d.get(sümbol, 0) + 1
    return d
    
    
def grupeeri(sõne):
    täishäälikud = "aeiouõäöüAEIOUÕÄÖÜ"
    
    d = {}
    for sümbol in sõne:
        d[sümbol] = d.get(sümbol, 0) + 1        
   # return d

    d2 = {"Täishäälikud": set(),
          "Kaashäälikud" : set(),
          "Muud" : set()}
    for võti in d:
        if võti in täishäälikud:
            d2["Täishäälikud"].add((võti, d[võti]))
        elif võti.isalpha() != True:
            d2["Muud"].add((võti, d[võti]))
        else:
            d2["Kaashäälikud"].add((võti, d[võti]))
    return(d2)
    