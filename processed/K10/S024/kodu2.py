def võitja(maatriks):
    X_loendur = 0
    O_loendur = 0
    rida = 4
    veerg = 4


    for i in range(rida):
        if maatriks[i][0] == maatriks[i][1] == maatriks[i][2] == "X":
            X_loendur += 1
        if maatriks[i][0] == maatriks[i][1] == maatriks[i][2] == "O":
            O_loendur += 1
        if maatriks[i][3] == maatriks[i][1] == maatriks[i][2] == "X":
             X_loendur += 1
        if maatriks[i][3] == maatriks[i][1] == maatriks[i][2] == "O":
            O_loendur += 1
    
    for j in range(veerg):
        if maatriks[0][j] == maatriks[1][j] == maatriks[2][j] == "X":
            X_loendur += 1
        if maatriks[0][j] == maatriks[1][j] == maatriks[2][j] == "O":
            O_loendur += 1
        if maatriks[3][j] == maatriks[1][j] == maatriks[2][j] == "X":
            X_loendur += 1
        if maatriks[3][j] == maatriks[1][j] == maatriks[2][j] == "O":
            O_loendur += 1
    
            
    if maatriks[0][0] == maatriks[1][1] == maatriks[2][2] == "X":
        X_loendur += 1
    if maatriks[0][0] == maatriks[1][1] == maatriks[2][2] == "O":
        O_loendur += 1
    if maatriks[3][3] == maatriks[1][1] == maatriks[2][2] == "X":
        X_loendur += 1
    if maatriks[3][3] == maatriks[1][1] == maatriks[2][2] == "O":
        O_loendur += 1
        


    if maatriks[0][3] == maatriks[1][2] == maatriks[2][1] == "X":
        X_loendur += 1
    if maatriks[0][3] == maatriks[1][2] == maatriks[2][1] == "O":
        O_loendur += 1
    if maatriks[3][0] == maatriks[1][2] == maatriks[2][1] == "X":
        X_loendur += 1
    if maatriks[3][0] == maatriks[1][2] == maatriks[2][1] == "O":
        O_loendur += 1
        
    if maatriks[0][1] == maatriks[1][2] == maatriks[2][3] == "X":
        X_loendur += 1
    if maatriks[0][1] == maatriks[1][2] == maatriks[2][3] == "O":
        O_loendur += 1
    if maatriks[1][0] == maatriks[3][2] == maatriks[2][1] == "X":
        X_loendur += 1
    if maatriks[1][0] == maatriks[3][2] == maatriks[2][1] == "O":
        O_loendur += 1
        
    if maatriks[0][2] == maatriks[1][1] == maatriks[2][0] == "X":
        X_loendur += 1
    if maatriks[0][2] == maatriks[1][1] == maatriks[2][0] == "O":
        O_loendur += 1
    if maatriks[1][3] == maatriks[2][2] == maatriks[3][1] == "X":
        X_loendur += 1
    if maatriks[1][3] == maatriks[2][2] == maatriks[3][1] == "O":
        O_loendur += 1
    
    
    
    sõnastik = {}
    sõnastik["O"] = O_loendur
    sõnastik["X"] = X_loendur
    
    return sõnastik
        
           