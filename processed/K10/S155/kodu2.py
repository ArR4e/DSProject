def võitja(maatriks):
    o_loendur = 0
    x_loendur = 0
    d = {'O': 0,'X': 0}
    i = 0
    j = 0
    
    for i in range(2):
        for j in range(4):
            if maatriks[i][j]==maatriks[i+1][j]==maatriks[i+2][j] == 'X':
                x_loendur += 1
            elif maatriks[i][j]==maatriks[i+1][j]==maatriks[i+2][j] == 'O':
                o_loendur += 1    
    for j in range(2):
        for i in range(4):
            if maatriks[i][j]==maatriks[i][j+1]==maatriks[i][j+2] == 'X':
                x_loendur += 1
            elif maatriks[i][j]==maatriks[i][j+1]==maatriks[i][j+2] == 'O':
                o_loendur += 1  
    ##########################################################################
    for i in range(2):
        for j in range(2):
            if maatriks[i][j]==maatriks[i+1][j+1]==maatriks[i+2][j+2] == 'X':
                x_loendur += 1
            elif maatriks[i][j]==maatriks[i+1][j+1]==maatriks[i+2][j+2] == 'O':
                o_loendur += 1  
    for j in range(2):
        for i in range(2):
            if maatriks[i][j+2]==maatriks[i+1][j+1]==maatriks[i+2][j] == 'X':
                x_loendur += 1
            elif maatriks[i][j+2]==maatriks[i+1][j+1]==maatriks[i+2][j] == 'O':
                o_loendur += 1  
   
    d['O'] = o_loendur
    d['X'] = x_loendur
    return d