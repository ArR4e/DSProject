def võitja(maatriks):
    sõnastik = {}
    X_arv = 0
    O_arv = 0
    for i in range(4):
        for j in range(2):
            gruppide_summa = maatriks[i][j] + maatriks[i][j+1] + maatriks[i][j+2]
            if gruppide_summa == 'XXX':
                X_arv += 1
            if gruppide_summa == 'OOO':
                O_arv += 1
    for i in range(2):
        for j in range(4):
            gruppide_summa = maatriks[i][j] + maatriks[i+1][j] + maatriks[i+2][j]
            if gruppide_summa == 'XXX':
                X_arv += 1
            if gruppide_summa == 'OOO':
                O_arv += 1
    for i in range(2):
        for j in range(2):
            gruppide_summa = maatriks[i][j] + maatriks[i+1][j+1] + maatriks[i+2][j+2]
            if gruppide_summa == 'XXX':
                X_arv += 1
            if gruppide_summa == 'OOO':
                O_arv += 1
    for i in range(2):
        for j in range(2):
            gruppide_summa = maatriks[i][j+2] + maatriks[i+1][j+1] + maatriks[i+2][j]
            if gruppide_summa == 'XXX':
                X_arv += 1
            if gruppide_summa == 'OOO':
                O_arv += 1
    sõnastik = {'O': O_arv, 'X': X_arv}
    return sõnastik