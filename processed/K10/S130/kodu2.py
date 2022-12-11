def võitja(maatriks):
    X_loendus = 0
    O_loendus = 0
    muu_mark = 0
    a = {}
    for i in range(4):
        for j in range(2):
            esimene = maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2]
            if esimene == True:
                if maatriks[i][j] == 'X':
                    X_loendus += 1
                elif maatriks[i][j] == 'O':
                    O_loendus += 1
                else:
                    muu_mark += 1
                    
    for i in range(2):
        for j in range(4):
            esimene = maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j]
            if esimene == True:
                if maatriks[i][j] == 'X':
                    X_loendus += 1
                elif maatriks[i][j] == 'O':
                    O_loendus += 1
                else:
                    muu_mark += 1
                    
    for i in range(2):
        for j in range(2):
            algus = maatriks[i][j] == maatriks[i+1][j+1] == maatriks [i+2][j+2]
            if algus == True:
                if maatriks[i][j] == 'X':
                    X_loendus += 1
                elif maatriks[i][j] == 'O':
                    O_loendus += 1
                else:
                    muu_mark += 1
    
    for i in range(2):
        for j in range(2,4):
            algus = maatriks[i][j] == maatriks[i+1][j-1] == maatriks [i+2][j-2]
            if algus == True:
                if maatriks[i][j] == 'X':
                    X_loendus += 1
                elif maatriks[i][j] == 'O':
                    O_loendus += 1
                else:
                    muu_mark += 1
     
    a['O'] = O_loendus
    a['X'] = X_loendus
                    
    return(a)
