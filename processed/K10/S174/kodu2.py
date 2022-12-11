def võitja(maatriks):
    sõnastik = {}
    X_loendur = 0
    O_loendur = 0
    summa = 0
    for i in range(4):
        for j in range(2):
            summa = maatriks[i][j] + maatriks[i][j + 1] + maatriks[i][j + 2]
            if summa == "XXX":
                X_loendur += 1
            if summa == "OOO":
                O_loendur += 1
                
    for i in range(2):
        for j in range(4):
            summa = maatriks[i][j] + maatriks[i + 1][j] + maatriks[i + 2][j]
            if summa == "XXX":
                X_loendur += 1
            if summa == "OOO":
                O_loendur += 1
    
    for i in range(2):
        for j in range(2):
            summa = maatriks[i][j] + maatriks[i + 1][j + 1] + maatriks[i + 2][j + 2]
            if summa == "XXX":
                X_loendur += 1
            if summa == "OOO":
                O_loendur += 1
                
    for i in range(2):
        for j in range(2):
            summa = maatriks[i][j + 2] + maatriks[i + 1][j + 1] + maatriks[i + 2][j]
            if summa == "XXX":
                X_loendur += 1
            if summa == "OOO":
                O_loendur += 1
                
    sõnastik = {"0": O_loendur, "X": X_loendur}           
    return sõnastik

        

            

