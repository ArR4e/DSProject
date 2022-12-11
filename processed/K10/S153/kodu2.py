def võitja(maatriks):
    sõnastik = {}
    X_loendur = 0
    O_loendur = 0
    key1 = "X"
    key2 = "O"
    for nimekiri in maatriks:
        for i in range(2):
            for j in range(2):
                if maatriks[i][j]+maatriks[i][j+1]+maatriks[i][j+2] == "XXX":
                    X_loendur += 1
                elif maatriks[i][j]+maatriks[i][j+1]+maatriks[i][j+2] == "OOO":
                    O_loendur += 1
        for i in range(2):
            for j in range(2):
                if maatriks[i][j]+maatriks[i+1][j]+maatriks[i+2][j] == "XXX":
                    X_loendur += 1
                elif maatriks[i][j]+maatriks[i+1][j]+maatriks[i+2][j] == "OOO":
                    O_loendur += 1
        for i in range(2):
            for j in range(2):
                if maatriks[i][j]+maatriks[i+1][j+1]+maatriks[i+2][j+2] == "XXX":
                    X_loendur += 1
                elif maatriks[i][j]+maatriks[i+1][j+1]+maatriks[i+2][j+2] == "OOO":
                    O_loendur += 1
        sõnastik["X"] = X_loendur//4
        sõnastik["O"] = O_loendur//4
    return sõnastik