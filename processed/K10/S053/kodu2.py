def võitja(maatriks):
    sõnastik = {}
    x_loendur = 0
    o_loendur = 0
    tühi = 0
    n = len(maatriks)
    
    #rida
    for i in range(n):
        for j in range(n-2):
            if maatriks[i][j]==maatriks[i][j+1]==maatriks[i][j+2] == "X":
                x_loendur += 1
            elif maatriks[i][j]==maatriks[i][j+1]==maatriks[i][j+2] == "O":
                o_loendur += 1
            else:
                tühi += 1
    #veerg
    for i in range(n-2):
        for j in range(n):
            if maatriks[i][j]==maatriks[i+1][j]==maatriks[i+2][j] == "X":
                x_loendur += 1
            elif maatriks[i][j]==maatriks[i+1][j]==maatriks[i+2][j] == "O":
                o_loendur += 1
            else:
                tühi += 1
                
    #peadiagonaal
    for i in range(n-2):
        for j in range(n-2):
            if maatriks[i][j]==maatriks[i+1][j+1]==maatriks[i+2][j+2] == "X":
                x_loendur += 1
            elif maatriks[i][j]==maatriks[i+1][j+1]==maatriks[i+2][j+2] == "O":
                o_loendur += 1
            else:
                tühi += 1

    #kõrvaldiagonaal
    for i in range(n-2):
        for j in range(n-2):
            if maatriks[i+2][j]==maatriks[i+1][j+1]==maatriks[i][j+2] == "X":
                x_loendur += 1
            elif maatriks[i+2][j]==maatriks[i+1][j+1]==maatriks[i][j+2] == "O":
                o_loendur += 1
            else:
                tühi += 1
                
    sõnastik["X"] = x_loendur
    sõnastik["O"] = o_loendur
    
    return sõnastik

võitja([['O',' ','O','X'],
        ['O','O','X','X'],
        ['O','X','O',' '],
        ['X','X','X','O']])