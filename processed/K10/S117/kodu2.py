#alustasin 30.10.2021 (23:02)
def võitja(maatriks):
    X_loendur = 0
    O_loendur = 0
    #read
    for i in range(4):
        for j in range(2):
            sumbol = maatriks[i][j] + maatriks[i][j + 1] + maatriks[i][j + 2]
            if sumbol == 'OOO':
                O_loendur += 1
            elif sumbol == 'XXX':
                X_loendur += 1
    #veerud
    for j in range(4):
        for i in range(2):
            sumbol = maatriks[i][j] + maatriks[i + 1][j] + maatriks[i + 2][j]
            if sumbol == 'OOO':
                O_loendur += 1
            elif sumbol == 'XXX':
                X_loendur += 1
    #põhidiagonaal \
    for i in range(2):
        sumbol = maatriks[i][i] + maatriks[i + 1][i + 1] + maatriks[i + 2][i + 2]
        if sumbol == 'OOO':
            O_loendur += 1
        elif sumbol == 'XXX':
            X_loendur += 1
    #põhidiagonaal / #kontrollime diagonaali, mis läheb paremalt - vasakule
    j = 3 #sellepärast alustame sellega, et j = 3
    for i in range(2):
        sumbol = maatriks[i][j] + maatriks[i + 1][j - 1] + maatriks[i + 2][j - 2]
        if sumbol == 'OOO':
            O_loendur += 1
        elif sumbol == 'XXX':
            X_loendur += 1
        j -= 1 
    #kõrvaldiagonaal
    for i in range(2):
        for j in range(2):
            if i == j:
                sumbol = maatriks[i][j + 2] + maatriks[i + 1][j + 1] + maatriks[i + 2][j]
                if sumbol == 'OOO':
                    O_loendur += 1
                elif sumbol == 'XXX':
                    X_loendur += 1
            else:
                sumbol = maatriks[i][j] + maatriks[i + 1][j + 1] + maatriks[i + 2][j + 2]
                if sumbol == 'OOO':
                    O_loendur += 1
                elif sumbol == 'XXX':
                    X_loendur += 1
    sõnastik = {'O':O_loendur,'X':X_loendur}
    return sõnastik