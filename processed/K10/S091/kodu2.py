def võitja(maatriks):
    tulemus = {}
    x = 0
    o = 0
    for i in range(4):
        for j in range(2):
            if maatriks[i][j]==maatriks[i][j+1]==maatriks[i][j+2]=='X':#rida
                x += 1
            elif maatriks[i][j]==maatriks[i][j+1]==maatriks[i][j+2]=='O':
                o += 1
    for i in range(2):
        for j in range(4):
            if maatriks[i][j]==maatriks[i+1][j]==maatriks[i+2][j]=='X':#veerg
                x += 1
            elif maatriks[i][j]==maatriks[i+1][j]==maatriks[i+2][j]=='O':
                o += 1
    for i in range(2):
        for j in range(2):
            if maatriks[i][j]==maatriks[i+1][j+1]==maatriks[i+2][j+2]=='X':#peadiagonaal
                x += 1
            elif maatriks[i][j]==maatriks[i+1][j+1]==maatriks[i+2][j+2]=='O':
                o += 1    
    for i in range(3,1,-1):
        for j in range(2):
            if maatriks[i][j] == maatriks[i-1][j+1] == maatriks[i-2][j+2]=='X':#korvaldiagonaal
                x += 1
            if maatriks[i][j] == maatriks[i-1][j+1] == maatriks[i-2][j+2] =='O':
                o += 1
    tulemus['O'] = o
    tulemus['X'] = x
    return tulemus

võitja([['O',' ','O','X'],
        ['O','O','X','X'],
        ['O','X','O',' '],
        ['X','X','X','O']])

