poisid_ja_tüdrukud = ['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']

def poisse_ja_tüdrukuid(järjend):
    poisid = 0
    tüdrukud = 0
    for el in järjend:
        sugu = el[-1]
        if sugu == "P":
            poisid += 1
        else:
            tüdrukud += 1
        ennik = (poisid, tüdrukud)
    return ennik

print(poisse_ja_tüdrukuid(poisid_ja_tüdrukud))

