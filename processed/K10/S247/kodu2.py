def võitja(maatriks):
    sõnastik = {}
    kokku = 0
    X_loendur = 0
    O_loendur = 0

    for i in range(4):
        for j in range(2):
            kokku = maatriks[i][j] + maatriks[i][j + 1] + maatriks[i][j + 2]
            if kokku == "XXX":
                X_loendur += 1
            elif kokku == "OOO":
                    O_loendur += 1
                
    for i in range(2):
        for j in range(4):
            kokku = maatriks[i][j] + maatriks[i + 1][j] + maatriks[i + 2][j]
            if kokku == "XXX":
                X_loendur += 1
            elif kokku == "OOO":
                O_loendur += 1
                    
    for i in range(2):
        for j in range(2):
            kokku = maatriks[i][j] + maatriks[i + 1][j +1] + maatriks[i + 2][j + 2]
            if kokku == "XXX":
                X_loendur += 1
            elif kokku == "OOO":
                O_loendur += 1
                    
    for i in range(2):
        for j in range(2):
            kokku = maatriks[i][j + 2] + maatriks[i + 1][j + 1] + maatriks[i + 2][j]        
            if kokku == "XXX":
                X_loendur += 1
            elif kokku == "OOO":
                    O_loendur += 1
                    
    sõnastik = {"O": O_loendur, "X": X_loendur}
    return sõnastik