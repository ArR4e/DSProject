def poisse_ja_tüdrukuid(nimekiri):
    poisse = 0
    tüdrukuid = 0
    for laps in nimekiri:
        if laps[-1] == "P":
            poisse+=1
        elif laps[-1] == "T":
            tüdrukuid+=1
    tulemus_ennik = (poisse, tüdrukuid)
    return(tulemus_ennik)

#print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))