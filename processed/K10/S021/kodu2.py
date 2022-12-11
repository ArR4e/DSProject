def võitja(maatriks):
    sõnastik = {}
    X_loendur = 0
    O_loendur = 0
    for i in range(len(maatriks)):
        for j in range(len(maatriks)-2):
            if maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2]:
                if maatriks[i][j] == "X":
                    X_loendur += 1
                elif maatriks[i][j] == "O":
                    O_loendur += 1
    
    for i in range(len(maatriks)-2):
        for j in range(len(maatriks)):
            if maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j]:
                if maatriks[i][j] == "X":
                    X_loendur += 1
                elif maatriks[i][j] == "O":
                    O_loendur += 1
                    
    if maatriks[0][0] == maatriks[1][1] == maatriks[2][2] == "X":
        X_loendur += 1
    if maatriks[1][1] == maatriks[2][2] == maatriks[3][3] == "X":
        X_loendur += 1
    if maatriks[0][0] == maatriks[1][1] == maatriks[2][2] == "O":
        O_loendur += 1
    if maatriks[1][1] == maatriks[2][2] == maatriks[3][3] == "O":
        O_loendur += 1
    if maatriks[0][3] == maatriks[1][2] == maatriks[2][1] == "X":
        X_loendur += 1
    if maatriks[1][2] == maatriks[2][1] == maatriks[3][0] == "X":
        X_loendur += 1
    if maatriks[0][3] == maatriks[1][2] == maatriks[2][1] == "O":
        O_loendur += 1
    if maatriks[1][2] == maatriks[2][1] == maatriks[3][0] == "O":
        O_loendur += 1
    if maatriks[1][0] == maatriks[2][1] == maatriks[3][2] == "X":
        X_loendur += 1
    if maatriks[1][0] == maatriks[2][1] == maatriks[3][2] == "O":
        O_loendur += 1
    if maatriks[0][1] == maatriks[1][2] == maatriks[2][3] == "X":
        X_loendur += 1
    if maatriks[0][1] == maatriks[1][2] == maatriks[2][3] == "O":
        O_loendur += 1
    if maatriks[0][2] == maatriks[1][1] == maatriks[2][0] == "X":
        X_loendur += 1
    if maatriks[0][2] == maatriks[1][1] == maatriks[2][0] == "O":
        O_loendur += 1
    if maatriks[1][3] == maatriks[2][2] == maatriks[3][1] == "X":
        X_loendur += 1
    if maatriks[1][3] == maatriks[2][2] == maatriks[3][1] == "O":
        O_loendur += 1
        
    sõnastik["X"] = X_loendur
    sõnastik["O"] = O_loendur
    return sõnastik