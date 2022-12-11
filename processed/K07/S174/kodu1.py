#sain abi konsultatsioonist ja murelahendajalt
def poisse_ja_tüdrukuid(järjend):
    tüdrukuid = 0
    poisse = 0
    if täht == "T":
        tüdrukuid += 1
    else:
        poisse += 1
    return(tüdrukuid, poisse)
                
s = poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T'])
print(s)