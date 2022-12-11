def võitja(maatriks):
    X_loendur = 0    
    O_loendur = 0   
    for i in range(4):
        for j in range(2):
            sümbol = maatriks[i][j]+maatriks[i][j+1]+maatriks[i][j+2]
            if sümbol == "XXX":
                X_loendur += 1
            elif sümbol == "OOO":
                O_loendur += 1
    for i in range(2):
        for j in range(4):
            sümbol = maatriks[i][j]+maatriks[i+1][j]+maatriks[i+2][j]
            if sümbol == "XXX":
                X_loendur += 1
            elif sümbol == "OOO":
                O_loendur += 1
    for i in range(2):
        for j in range(2):
            sümbol = maatriks[i][j]+maatriks[i+1][j+1]+maatriks[i+2][j+2]
            if sümbol == "XXX":
                X_loendur += 1
            elif sümbol == "OOO":
                O_loendur += 1
    for i in range(2):
        for j in range(2):
            sümbol = maatriks[i][j+2]+maatriks[i+1][j+1]+maatriks[i+2][j]
            if sümbol == "XXX":
                X_loendur += 1
            elif sümbol == "OOO":
                O_loendur += 1
    sõnastik = {}
    sõnastik["X"] = set()
    sõnastik["X"] = X_loendur
    sõnastik["O"] = set()
    sõnastik["O"] = O_loendur
    return sõnastik
