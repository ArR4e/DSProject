def võitja(maatriks):
    X_loendur = 0
    O_loendur = 0
    sümbol1 = "X"
    sümbol2 = "O"
    sõnastik = {}
    sõnastik["X"] = set()
    sõnastik["O"] = set()
    #ridade lugemine
    for i in range(4):
        for j in range(2):
            if maatriks[i][j]==maatriks[i][j+1]==maatriks[i][j+2]== sümbol1:
                X_loendur += 1
            if maatriks[i][j]==maatriks[i][j+1]==maatriks[i][j+2]== sümbol2:
                O_loendur += 1
    #veergude lugemine
    for i in range(2):
        for j in range(4):
            if maatriks[i][j]==maatriks[i+1][j]==maatriks[i+2][j]== sümbol1:
                X_loendur += 1
            if maatriks[i][j]==maatriks[i+1][j]==maatriks[i+2][j]== sümbol2:
                O_loendur += 1
    #peadiagonaali lugemine
    for i in range(2):
        for j in range(2):
            if maatriks[i][j]==maatriks[i+1][j+1]==maatriks[i+2][j+2]== sümbol1:
                X_loendur += 1
            if maatriks[i][j]==maatriks[i+1][j+1]==maatriks[i+2][j+2]== sümbol2:
                O_loendur += 1
    #kõrvaldiagonaali lugemine
    for i in range(2):
        for j in range(2):
            if maatriks[i][j+2]==maatriks[i+1][j+1]==maatriks[i+2][j]== sümbol1:
                X_loendur += 1
            if maatriks[i][j+2]==maatriks[i+1][j+1]==maatriks[i+2][j]== sümbol2:
                O_loendur += 1
    sõnastik["X"] = X_loendur
    sõnastik["O"] = O_loendur
    sõnastik2 = {"X":sõnastik["X"], "O":sõnastik["O"]}
    return sõnastik2
