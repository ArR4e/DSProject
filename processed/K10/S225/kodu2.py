def võitja(maatriks):
    sõnastik = {}
    sõnastik['O'] = 0
    sõnastik['X'] = 0
    for i in range(2):
        for j in range(2):
            #read
            if (maatriks[i][j] ==  maatriks[i][j+1] ==  maatriks[i][j+2] == 'X'):
                sõnastik['X'] += 1
            if (maatriks[i][j] ==  maatriks[i][j+1] ==  maatriks[i][j+2] == 'O'):
                sõnastik['O'] += 1
            if (maatriks[i+2][j] ==  maatriks[i+2][j+1] ==  maatriks[i+2][j+2] == 'X'):
                sõnastik['X'] += 1
            if (maatriks[i+2][j] ==  maatriks[i+2][j+1] ==  maatriks[i+2][j+2] == 'O'):
                sõnastik['O'] += 1
            #vertikaal
            if (maatriks[i][j] ==  maatriks[i+1][j+1] == maatriks[i+2][j+2] == 'O'):
                sõnastik['O'] += 1
            if (maatriks[i][j] ==  maatriks[i+1][j+1] == maatriks[i+2][j+2] == 'X'):
                sõnastik['X'] += 1
            if (maatriks[i+2][j] ==  maatriks[i+1][j+1] == maatriks[i][j+2] == 'O'):
                sõnastik['O'] += 1
            if (maatriks[i][j+2] ==  maatriks[i+1][j+1] == maatriks[i+2][j] == 'X'):
                sõnastik['X'] += 1
            #ülevalt alla
            if (maatriks[i][j] ==  maatriks[i+1][j] ==  maatriks[i+2][j] == 'X'):
                sõnastik['X'] += 1
            if (maatriks[i][j] ==  maatriks[i+1][j] ==  maatriks[i+2][j] == 'O'):
                sõnastik['O'] += 1
            if (maatriks[i][j+2] ==  maatriks[i+1][j+2] ==  maatriks[i+2][j+2] == 'X'):
                sõnastik['X'] += 1
            if (maatriks[i][j+2] ==  maatriks[i+1][j+2] ==  maatriks[i+2][j+2] == 'O'):
                sõnastik['O'] += 1
    return sõnastik