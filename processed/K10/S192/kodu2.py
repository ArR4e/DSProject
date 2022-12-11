def võitja(maatriks): # maatriks on järjendite järjend
    punktid = {}
    O = uuri('O', maatriks)
    X = uuri('X', maatriks)
    punktid['O'] = O
    punktid['X'] = X
    return punktid
    
def uuri(sümbol, maatriks):
    esinemise_arv = 0
    korda_3 = sümbol*3
    # Horistonaalne kontroll
    for i in range(4): # Read indeksidega 0-3 ehk 4 rida
        for j in range(2): # Siin 2, kuna liidame indeksile viimases liidetavas 2 juurde: maatriks[i][j+2]
            summa = maatriks[i][j]+maatriks[i][j+1]+maatriks[i][j+2]
            if korda_3 == summa:
                esinemise_arv += 1

    # Vertikaalne kontroll
    for i in range(2): # Siin 2, kuna liidame indeksile viimases liidetavas 2 juurde: maatriks[i+2][j]
        for j in range(4): # Veerud indeksidega 0-3 ehk 4 veergu
            summa = maatriks[i][j]+maatriks[i+1][j]+maatriks[i+2][j]
            if korda_3 == summa:
                esinemise_arv += 1

    # Diagonaalne kontroll
    for i in range(2): # Siin 2, kuna liidame indeksile viimases liidetavas 2 juurde: maatriks[i+2][j+2]
        for j in range(2): # Siin 2, kuna liidame indeksile viimases liidetavas 2 juurde: maatriks[i+2][j+2]
            summa = maatriks[i][j]+maatriks[i+1][j+1]+maatriks[i+2][j+2]
            if korda_3 == summa:
                esinemise_arv += 1

    # Kõrvaldiagonaalne kontroll
    for i in range(2): # Siin 2, kuna liidame indeksile viimases liidetavas 2 juurde: maatriks[i+2][j]
        for j in range(2): # Siin 2, kuna liidame indeksile esimeses liidetavas 2 juurde: maatriks[i][j+2]
            summa = maatriks[i][j+2]+maatriks[i+1][j+1]+maatriks[i+2][j]
            if korda_3 == summa:
                esinemise_arv += 1
    
    return esinemise_arv