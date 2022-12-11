def võitja(a):
    X1 = 0
    Y1 = 0
    for i in range(len(a)):
        for j in range(len(a)):
            try:
                if  j < 2:
                    if a[i][j] == a[i][j+1] == a[i][j+2] == 'X':
                        X1 = X1 + 1
                if  j < 2:
                    if a[i][j] == a[i][j+1] == a[i][j+2] == 'O':
                        Y1 = Y1 + 1
                if i<2:
                    if a[i][j] == a[i+1][j] == a[i+2][j] == 'X':
                        X1 = X1 + 1
                if i<2:
                    if a[i][j] == a[i+1][j] == a[i+2][j] == 'O':
                        Y1 = Y1 + 1
                if i < 2 and j <2:
                    if a[i][j] == a[i+1][j+1] == a[i+2][j+2] =='X':
                         X1 = X1 + 1
                if i < 2 and j <2:
                    if a[i][j] == a[i+1][j+1] == a[i+2][j+2] =='O':
                        Y1 = Y1 + 1
                if i < 2 and j >1:        
                    if a[i][j] == a[i+1][j-1] == a[i+2][j-2] =='X':
                        X1 = X1 + 1
                if i < 2 and j >1:
                    if a[i][j] == a[i+1][j-1] == a[i+2][j-2] =='O':
                        Y1 = Y1 + 1
            except:
                continue
    nkiri = {}
    nkiri["X"] = X1
    nkiri["O"] = Y1
    return nkiri

võitja([['O',' ',' ','X'],
        [' ','O','X',' '],
        [' ','X','O',' '],
        ['X',' ',' ','O']])