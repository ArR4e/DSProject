def võitja(maatriks):
    X = 0
    O = 0
    s = {}
    for i in range(3):
        for j in range(1):
            if (maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2]) == True:
                X += 1
    for i in range(1):
        for j in range(3):
            if (maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j] == 'X') == True:
                X += 1
    for i in range(1):
        for j in range(1):
            if (maatriks[i][j] == maatriks[i+1][j+1] == maatriks[i+2][j+2] == 'X') == True:
                X += 1
    for i in range(0):
        for j in range(0):
            if (maatriks[i+1][j] == maatriks[i+2][j+1] == maatriks[i+3][j+2] == 'X') == True:
                X += 1
    for i in range(1):
        for j in range(1):
            if (maatriks[i][j+2] == maatriks[i+1][j+1] == maatriks[i+2][j] == 'X') == True:
                X += 1
    for i in range(3):
        for j in range(1):
            if (maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2]) == True:
                X += 1
    for i in range(1):
        for j in range(3):
            if (maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j] == 'O') == True:
                O += 1
    for i in range(1):
        for j in range(1):
            if (maatriks[i][j] == maatriks[i+1][j+1] == maatriks[i+2][j+2] == 'O') == True:
                O += 1
    for i in range(0):
        for j in range(0):
            if (maatriks[i+1][j] == maatriks[i+2][j+1] == maatriks[i+3][j+2] == 'O') == True:
                O += 1
    for i in range(1):
        for j in range(1):
            if (maatriks[i][j+2] == maatriks[i+1][j+1] == maatriks[i+2][j] == 'O') == True:
                O += 1
    s['X'] = X
    s['O'] = O
    return s
     
print(võitja([['X','X','X','='],
        [' ','X',' ','O'],
        ['X','X','O','O'],
        [' ','O','X','X']]))

