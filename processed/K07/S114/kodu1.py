
def poisse_ja_tüdrukuid(nimed):
    poisid = 0
    tüdrukud = 0
    for rida in nimed:
        read = rida.split(" ")
        if read[-1] == "P":
            poisid += 1
        elif read[-1] == "T":
            tüdrukud += 1
    return poisid,tüdrukud
        
print(poisse_ja_tüdrukuid(['Mati P', 'Kati P', 'Siim Aleksander P', 'Jüri P', 'Veronika P']))