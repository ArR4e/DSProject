def võitja(maatriks):
    sonastik = {}
    Od = 0
    Xd = 0
    for i in range(4):
        for j in range(2):
            if maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2] == "X":
                Xd += 1
            if maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2] == "O":
                Od += 1
    for j in range(4):
        for i in range(2):
            if maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j] == "X":
                Xd += 1
            if maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j] == "O":
                Od += 1
    for i in range(2):
        for j in range(3, 1, -1):
            if maatriks[j][i] == maatriks[j-1][i+1] == maatriks[j-2][i+2] == "X":
                Xd += 1
            if maatriks[j][i] == maatriks[j-1][i+1] == maatriks[j-2][i+2] == "O":
                Od += 1
            if maatriks[i][j-2] == maatriks[i+1][j-1] == maatriks[i+2][j] == "X":
                Xd += 1
            if maatriks[i][j-2] == maatriks[i+1][j-1] == maatriks[i+2][j] == "O":
                Od += 1
    sonastik["O"] = Od
    sonastik["X"] = Xd
    return sonastik

