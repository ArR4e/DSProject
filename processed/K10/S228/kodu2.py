def võitja(maatriks):
    X_n = 0
    O_n = 0
    tulemus = dict()
    tulemus['O'] = set()
    tulemus['X'] = set()
    for i in range(4): #rida
        for j in range(2):
            if maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2] == 'X':
                X_n += 1
            elif maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2] == 'O':
                O_n += 1
    for i in range(2): #veerg
        for j in range(4):
            if maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j] == 'X':
                X_n += 1
            elif maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j] == 'O':
                O_n += 1
    for i in range(2): #peadiagonaal
        for j in range(2):
            if maatriks[i][j] == maatriks[i+1][j+1] == maatriks[i+2][j+2] == 'X':
                X_n += 1
            elif maatriks[i][j] == maatriks[i+1][j+1] == maatriks[i+2][j+2] == 'O':
                O_n += 1
    for i in range(2): #kõrvaldiagonaal
        for j in range(2):
            if maatriks[i+2][j] == maatriks[i+1][j+1] == maatriks[i][j+2] == 'X':
                X_n += 1
            elif maatriks[i+2][j] == maatriks[i+1][j+1] == maatriks[i][j+2] == 'O':
                O_n += 1
    tulemus['O'] = O_n
    tulemus['X'] = X_n
    return(tulemus)