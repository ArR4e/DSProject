nimed = ['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']

def poisse_ja_tüdrukuid(järjend):
    poisid = 0
    tüdrukud = 0
    for i in järjend:
        sugu = i.split(' ')[-1]
        if sugu == 'P':
            poisid += 1
        if sugu == 'T':
            tüdrukud += 1
    ennik = (poisid, tüdrukud)
    return ennik

print(poisse_ja_tüdrukuid(nimed))
    