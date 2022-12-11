from math import ceil

def võitja(maatriks):
    dict = {'O': 0, 'X': 0}
    kordusO = 0
    kordusX = 0
    for i in range(4): #töötlen läbi read
        for j in range(2):
            if maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2] == 'X':
                kordusX += 1
            if maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2] == 'O':
                kordusO += 1
    for i in range(2): #töötlen läbi veerud
        for j in range(4):
            if maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j] == 'X':
                kordusX += 1
            if maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j] == 'O':
                kordusO += 1
    for i in range(2): #töötlen läbi peadiagonaali
        for j in range(2):
            if maatriks[i][j] == maatriks[i+1][j+1] == maatriks[i+2][j+2] == 'X':
                kordusX += 1
            if maatriks[i][j] == maatriks[i+1][j+1] == maatriks[i+2][j+2] == 'O':
                kordusO += 1
    for i in range(2): #töötlen läbi korvaldiagonaali
        for j in range(2):
            if maatriks[i][j+2] == maatriks[i+1][j+1] == maatriks[i+2][j] == 'X':
                kordusX += 1
            if maatriks[i][j+2] == maatriks[i+1][j+1] == maatriks[i+2][j] == 'O':
                kordusO += 1
    dict['O'] = kordusO
    dict['X'] = kordusX
    return dict

print(võitja([['O',' ','O','X'],
            ['O','O','X','X'],
            ['O','X','O',' '],
            ['X','X','X','O']]))