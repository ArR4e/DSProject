def võitja(maatriks):
    X_loendur = 0
    O_loendur = 0
    X_arv = 0
    O_arv = 0
    seis = {}
    for sümbol in maatriks:
        if sümbol == 'X':
            X_loendur += 1
        if sümbol == 'O':
            O_loendur += 1
    for i in range(3):
        for j in range(3):
            if maatriks[i][j]==maatriks[i+1][j]==maatriks[i+2][j]=='X':
                X_arv += 1
            if maatriks[i][j]==maatriks[i+1][j]==maatriks[i+2][j]=='O':
                O_arv += 1
            if maatriks[i][j]==maatriks[i+1][j+1]==maatriks[i+1][j+1]=='X':
                X_arv += 1
            if maatriks[i][j]==maatriks[i+1][j+1]==maatriks[i+1][j+1]=='O':
                O_arv += 1
            if maatriks[i][j]==maatriks[i][j+1]==maatriks[i][j+2]=='X':
                X_arv += 1
            if maatriks[i][j]==maatriks[i][j+1]==maatriks[i][j+2]=='O':
                O_arv += 1
            if maatriks[i][j+2]==maatriks[i+1][j+1]==maatriks[i+2][j]=='X':
                X_arv += 1
            if maatriks[i][j+2]==maatriks[i+1][j+1]==maatriks[i+2][j]=='O':
                O_arv += 1
            if maatriks[i][j+1]==maatriks[i+1][j+2]==maatriks[i+2][j+3]=='X':
                X_arv += 1
            if maatriks[i][j+1]==maatriks[i+1][j+2]==maatriks[i+2][j+3]=='O':
                O_arv += 1
    seis['X'] = X_arv
    seis['O'] = O_arv
    return seis


võitja([['O',' ','O','X'],
            ['O','O','X','X'],
            ['O','X','O',' '],
            ['X','X','X','O']])
            
            