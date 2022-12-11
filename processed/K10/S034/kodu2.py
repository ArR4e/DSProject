def võitja(maatriks):
    X_loendur = 0
    O_loendur = 0
    #HORISONTAALNE LOENDUS
    for i in range(4):
        for j in range(2):
            if maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2] == "X":
                X_loendur += 1
    for i in range(4):
        for j in range(2):
            if maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2] == "O":
                O_loendur += 1
    #VERTIKAALNE LOENDUS
    for i in range(2):
        for j in range(4):
            if maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j] == "X":
                X_loendur += 1
    for i in range(2):
        for j in range(4):
            if maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j] == "O":
                O_loendur += 1
    #DIAGONAALNE LOENDUS (PÕHIDIAGONAAL)
    for i in range(2):
        for j in range(2):
            if maatriks[i][j] == maatriks[i+1][j+1] == maatriks[i+2][j+2] == "X":
                X_loendur += 1
    for i in range(2):
        for j in range(2):
            if maatriks[i][j] == maatriks[i+1][j+1] == maatriks[i+2][j+2] == "O":
                O_loendur += 1
    #DIAGONAALNE LOENDUS (KÕRVALDIAGONAAL)
    for i in range(2):
        for j in range(2):
            if maatriks[i+2][j] == maatriks[i+1][j+1] == maatriks[i][j+2] == "X":
                X_loendur += 1
    for i in range(2):
        for j in range(2):
            if maatriks[i+2][j] == maatriks[i+1][j+1] == maatriks[i][j+2] == "O":
                O_loendur += 1 
    #koostame sõnastiku
    sõnastik = {}
    sõnastik['O'] = O_loendur
    sõnastik['X'] = X_loendur
    return sõnastik