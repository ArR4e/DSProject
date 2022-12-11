def võitja(maatriks):
    x_loendur = 0
    o_loendur = 0
    tulem = {}
    i = 0
    #X ja O maatriksi ridades
    for j in range(1):
        if maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2] == maatriks[i][j+3] == 'X':
            x_loendur += 2
        elif maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2] == 'X' or \
                            maatriks[i][j+1] == maatriks[i][j+2] == maatriks[i][j+3] == 'X':
            x_loendur += 1

        elif maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2] == maatriks[i][j+3] == 'O':
            o_loendur += 2
        if maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2] == 'O' or \
                            maatriks[i][j+1] == maatriks[i][j+2] == maatriks[i][j+3] == 'O':
            o_loendur += 1
    #X ja O maatriksi veergudes
    for k in range(4):                
        if maatriks[i][k] == maatriks[i+1][k] == maatriks[i+2][k] == maatriks[i+3][k] == 'X':
            x_loendur += 2
        elif maatriks[i][k] == maatriks[i+1][k] == maatriks[i+2][k] == 'X' or \
                            maatriks[i+1][k] == maatriks[i+2][k] == maatriks[i+3][k] == 'X':
            x_loendur += 1

        elif maatriks[i][k] == maatriks[i+1][k] == maatriks[i+2][k] == maatriks[i+3][k] == 'O':
            o_loendur += 2
        elif maatriks[i][k] == maatriks[i+1][k] == maatriks[i+2][k] == 'O' or \
                            maatriks[i+1][k] == maatriks[i+2][k] == maatriks[i+3][k] == 'O':
            o_loendur += 1
    #siit edasi ei loe ühes diagonaalis 2x, kui 4 sama väärtust
    #X ja O maatriksi diagonaalil \ suunas
    for l in range(1):                
        if maatriks[i][l] == maatriks[i+1][l+1] == maatriks[i+2][l+2] == 'X' or \
                            maatriks[i+1][l+1] == maatriks[i+2][l+2] == maatriks[i+3][l+3] == 'X' or \
                            maatriks[i][l+1] == maatriks[i+1][l+2] == maatriks[i+2][l+3] == 'X' or \
                            maatriks[i+1][l] == maatriks[i+2][l+1] == maatriks[i+3][l+2] == 'X':
            x_loendur += 1

        elif maatriks[i][l] == maatriks[i+1][l+1] == maatriks[i+2][l+2] == 'O' or \
                            maatriks[i+1][l+1] == maatriks[i+2][l+2] == maatriks[i+3][l+3] == 'O' or \
                            maatriks[i][l+1] == maatriks[i+1][l+2] == maatriks[i+2][l+3] == 'O' or \
                            maatriks[i+1][l] == maatriks[i+2][l+1] == maatriks[i+3][l+2] == 'O':
            o_loendur += 1
    #X ja O maatriksi diagonaalil / suunas
    for m in range(1):                
        if maatriks[i][m+3] == maatriks[i+1][m+2] == maatriks[i+2][m+1] == 'X' or \
                            maatriks[i+1][m+2] == maatriks[i+2][m+1] == maatriks[i+3][m] == 'X' or \
                            maatriks[i][m+2] == maatriks[i+1][m+1] == maatriks[i+2][m] == 'X' or \
                            maatriks[i+1][m+3] == maatriks[i+2][m+2] == maatriks[i+3][m+1] == 'X':
            x_loendur += 1

        elif maatriks[i][m+3] == maatriks[i+1][m+2] == maatriks[i+2][m+1] == 'O' or \
                            maatriks[i+1][m+2] == maatriks[i+2][m+1] == maatriks[i+3][m] == 'O' or \
                            maatriks[i][m+2] == maatriks[i+1][m+1] == maatriks[i+2][m] == 'O' or \
                            maatriks[i+1][m+3] == maatriks[i+2][m+2] == maatriks[i+3][m+1] == 'O':
            o_loendur += 1
        
    tulem['O'] = o_loendur
    tulem['X'] = x_loendur
    return tulem