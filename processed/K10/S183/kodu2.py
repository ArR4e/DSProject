def võitja(maatriks):
    O_lugeja = 0
    X_lugeja = 0
    sõnastik = {}

    for i in range(4):
        for j in range(4):
            try:
                m1 = maatriks[i][j] + maatriks[i][j+1] + maatriks[i][j+2]
                if m1 == "XXX":
                    X_lugeja += 1
                elif m1 == "OOO":
                    O_lugeja += 1
            except:
                pass
    for i in range(4):
        for j in range(4):
            try:
                m2 = maatriks[i][j] + maatriks[i+1][j] + maatriks[i+2][j]
                if m2 == "XXX":
                    X_lugeja += 1
                elif m2 == "OOO":
                    O_lugeja += 1
            except:
                pass
    for i in range(4):
        for j in range(4):
            try:
                m3 = maatriks[i][j] + maatriks[i+1][j+1] + maatriks[i+2][j+2]
                if m3 == "XXX":
                    X_lugeja += 1
                elif m3 == "OOO":
                    O_lugeja += 1
            except:
                pass
    for i in range(4):
        for j in range(4):
            try:
                m5 = maatriks[i][j+2] + maatriks[i+1][j+1] + maatriks[i+2][j]
                if m5 == "XXX":
                    X_lugeja += 1
                elif m5 == "OOO":
                    O_lugeja += 1
            except:
                pass
    sõnastik2 = {"O":O_lugeja, "X":X_lugeja}
    return sõnastik2
