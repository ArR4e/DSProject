def võitja(maatriks):
    sõnastik = {}
    X_loendur = 0 
    O_loendur = 0
    for i in range(4):
        for j in range(2):
            sümbol = maatriks[i][j] + maatriks[i][j+1] + maatriks[i][j+2]
            if sümbol == "XXX":
                X_loendur += 1
            elif sümbol == "OOO":
                O_loendur += 1
    for i in range(2):
        for j in range(4):
            sümbol = maatriks[i][j] + maatriks[i+1][j] + maatriks[i+2][j]
            if sümbol == "XXX":
                X_loendur += 1
            elif sümbol == "OOO":
                O_loendur += 1
    for i in range(2):
        for j in range(2):
            sümbol = maatriks[i][j] + maatriks[i+1][j+1] + maatriks[i+2][j+2]
            if sümbol == "XXX":
                X_loendur += 1
            elif sümbol == "OOO":
                O_loendur += 1
    for i in range(2):
        for j in range(3,1,-1):
            sümbol = maatriks[i][j] + maatriks[i+1][j-1] + maatriks[i+2][j-2]
            if sümbol == "XXX":
                X_loendur += 1
            elif sümbol == "OOO":
                O_loendur += 1
    sõnastik["O"] = O_loendur
    sõnastik["X"] = X_loendur
    
    return sõnastik