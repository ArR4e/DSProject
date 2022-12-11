# 1. Poiste ja tüdrukute arv

def poisse_ja_tüdrukuid(järjend):
    a = 0
    b = 0
    for sõne in järjend:
        if sõne[-1::] == "P":
            a += 1
        if sõne[-1::] == "T":
            b += 1
        return a, b
    
print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))