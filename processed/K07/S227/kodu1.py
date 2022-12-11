
def poisse_ja_tüdrukuid(järjend):
    poisid=0
    tüdrukud=0
    for i in järjend:
        jupid = i.split()
        nimi= jupid[0:-1]
        sugu= jupid[-1]
        if sugu == "T":
            tüdrukud+= 1
        elif sugu == "P":
            poisid+= 1
    return poisid, tüdrukud
#print(poisse_ja_tüdrukuid(['Mati P', 'Kati P', 'Siim Aleksander P', 'Jüri P', 'Veronika P']))
