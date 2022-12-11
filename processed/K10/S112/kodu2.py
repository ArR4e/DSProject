def võitja(maatriks):
    X_loendur = 0
    O_loendur = 0
    sõnastik = {}
    sõnastik["O"] = 0
    sõnastik["X"] = 0
    for rida in range(len(maatriks)):
        for veerg in range(len(maatriks[rida])):
            if maatriks[rida][veerg] == 'X':
                X_loendur += 1
            elif maatriks[rida][veerg] == 'O':
                O_loendur += 1
    print(X_loendur)
    print(O_loendur)
    
    for i in range(4):
        for j in range(2):
            reas = maatriks[i][j] + maatriks[i][j+1] + maatriks[i][j+2]
            
            if reas == "OOO":
                sõnastik["O"] += 1
            elif reas == "XXX":
                sõnastik["X"] += 1
    for i in range(2):
        for j in range(4):
            tulbas = maatriks[i][j] + maatriks[i+1][j] + maatriks[i+2][j]
            if tulbas == "OOO":
                sõnastik["O"] += 1
            elif tulbas == "XXX":
                sõnastik["X"] += 1
    for i in range(2):
        for j in range(2):
            diagonaalis = maatriks[i][j] + maatriks[i+1][j+1] + maatriks[i+2][j+2]
            if diagonaalis == "OOO":
                sõnastik["O"] += 1
            elif diagonaalis == "XXX":
                sõnastik["X"] += 1
    for i in range(2):
        for j in range(2):
            kõrval = maatriks[i][j+2] + maatriks[i+1][j+1] + maatriks[i+2][j]
            if kõrval == "OOO":
                sõnastik["O"] += 1
            elif kõrval == "XXX":
                sõnastik["X"] += 1
    return sõnastik
    
    
            