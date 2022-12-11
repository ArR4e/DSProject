järjend = ['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']

def poisse_ja_tüdrukuid(list):
    counterP = 0
    counterT = 0
    for i in list:
        if i[-1] == "P":
            counterP += 1
        elif i[-1] == "T":
            counterT += 1
    
    ennik = (counterP, counterT)
    return ennik

print(poisse_ja_tüdrukuid(järjend))