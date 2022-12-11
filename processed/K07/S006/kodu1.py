def poisse_ja_tüdrukuid(nimed):
    poisid = 0
    tütred = 0
    for nimi in nimed:
        list(nimi)
        if nimi[-1] == "P" and nimi[-2] == " ":
            poisid += 1
        elif nimi[-1] == "T" and nimi[-2] == " ":
            tütred += 1
        else:
            continue
    ennik = (poisid, tütred)
    return ennik
nimed = ['Mati P', 'Kati T', 'Siim AleksanderP', 'Jüri P', 'Veronika T']

print(str(poisse_ja_tüdrukuid(nimed)))