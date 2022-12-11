def horisontaal(maatriks, täht):
    summa = 0
    for i in range(len(maatriks)):
        for j in range(2):
            if maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2] == täht:
                summa += 1
    return summa
def vertikaal(maatriks, täht):
    summa = 0
    for i in range(2):
        for j in range(len(maatriks[0])):
            if maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j] == täht:
                summa += 1
    return summa
def peadiagonaal(maatriks, täht):
    summa = 0
    for i in range(2):
        for j in range(2):
            if maatriks[i][j] == maatriks[i+1][j+1] == maatriks[i+2][j+2] == täht:
                summa += 1
    return summa
def kõrvaldiagonaal(maatriks, täht):
    summa = 0
    for i in range(2):
        for j in range(2):
            if maatriks[i+2][j] == maatriks[i+1][j+1] == maatriks[i][j+2] == täht:
                summa += 1
    return summa
def võitja(maatriks):
    sõnastik = {}
    vertikaal_X = vertikaal(maatriks, "X")
    horisontaal_X = horisontaal(maatriks, "X")
    peadiagonaal_X = peadiagonaal(maatriks, "X")
    kõrvaldiagonaal_X = kõrvaldiagonaal(maatriks, "X")
    X_kogu = vertikaal_X + horisontaal_X + peadiagonaal_X + kõrvaldiagonaal_X
    vertikaal_O = vertikaal(maatriks, "O")
    horisontaal_O = horisontaal(maatriks, "O")
    peadiagonaal_O = peadiagonaal(maatriks, "O")
    kõrvaldiagonaal_O = kõrvaldiagonaal(maatriks, "O")
    O_kogu = vertikaal_O + horisontaal_O + peadiagonaal_O + kõrvaldiagonaal_O
    sõnastik["O"] = O_kogu
    sõnastik["X"] = X_kogu
    return sõnastik
                
                
              
 