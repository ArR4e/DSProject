maatriks = [[' ',' ',' ',' '],
            ['X',' ','O','X'],
            [' ','X','X',' '],
            ['X','X','X','X']]

def võitja(maatriks):
    sõnastik = {}
    oloendur = 0
    xloendur = 0
    for i in range(2):
        for j in range(4):
            if maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j] == "O":
                oloendur += 1
            if maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j] == "X":
                xloendur += 1
    for i in range(4):
        for j in range(2):
            if maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2] == "O":
                oloendur += 1
            if maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2] == "X":
                xloendur += 1
    for i in range(2):
        for j in range(2):
            if maatriks[i][j] == maatriks[i+1][j+1] == maatriks[i+2][j+2] == "O":
                oloendur += 1
            if maatriks[i][j] == maatriks[i+1][j+1] == maatriks[i+2][j+2] == "X":
                xloendur += 1
    for i in range(2):
        for j in range(2):
            if maatriks[i][j] == maatriks[i+1][j-1] == maatriks[i+2][j-2] == "O":
                oloendur += 1
            if maatriks[i][j] == maatriks[i+1][j-1] == maatriks[i+2][j-2] == "X":
                xloendur += 1
    sõnastik["O"] = oloendur
    sõnastik["X"] = xloendur
    return sõnastik

võitja(maatriks)