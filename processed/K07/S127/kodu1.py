def poisse_ja_tüdrukuid(järjend):
    poisse=0
    tüdrukuid=0
    for rida in järjend:
        sugu= rida[-1]
        if sugu =="P":
            poisse+=1
        else:
            tüdrukuid+=1
    return (poisse, tüdrukuid)
ennik =poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T'])
print(ennik)