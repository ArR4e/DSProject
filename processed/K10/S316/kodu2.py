def võitja(maatriks):
    seis = {}
    seis['O'] = set()
    seis['X'] = set()
    O_arv = 0
    X_arv = 0
    for i in range(4):
        for j in range(2):
            loendus_h = maatriks[i][j] + maatriks[i][j+1] + maatriks[i][j+2]
            if loendus_h == 'XXX':
                X_arv += 1
                seis['X'] = X_arv
            elif loendus_h == 'OOO':
                O_arv += 1
                seis['O'] = O_arv
    for i in range(2):
        for j in range(2):
            loendus_d = maatriks[i][j] + maatriks[i+1][j+1] + maatriks[i+2][j+2]
            if loendus_d == 'XXX':
                X_arv += 1
                seis['X'] = X_arv
            elif loendus_d == 'OOO':
                O_arv += 1
                seis['O'] = O_arv
            loendus_d2 = maatriks[i][j+2] + maatriks[i+1][j+1] + maatriks[i+2][j]
            if loendus_d2 == 'XXX':
                X_arv += 1
                seis['X'] = X_arv
            elif loendus_d2 == 'OOO':
                O_arv += 1
                seis['O'] = O_arv
    for i in range(2):
        for j in range(4):
            loendus_v = maatriks[i][j] + maatriks[i+1][j] + maatriks[i+2][j]
            if loendus_v == 'XXX':
                X_arv += 1
                seis['X'] = X_arv
            elif loendus_v == 'OOO':
                O_arv += 1
                seis['O'] = O_arv
    if X_arv == 0:
        seis['X'] = X_arv
    if O_arv == 0:
        seis['O'] = O_arv
    return seis