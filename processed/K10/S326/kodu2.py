def võitja(maatriks):
    võitja = {}
    x_loendur = 0
    o_loendur = 0
    for i in range(4):
        if maatriks[i][0] == maatriks[i][1] == maatriks[i][2]:
            if maatriks[i][0] == "X":
                x_loendur += 1
            elif maatrks[i][0] == "O":
                o_loendur += 1
        if maatriks[i][1] == maatriks[i][2] == maatriks[i][3]:
            if maatriks[i][1] == "X":
                x_loendur += 1
            elif maatriks[i][1] == "O":
                o_loendur += 1
    for i in range(4):
        if maatriks[0][i] == maatriks[1][i] == maatriks[2][i]:
            if maatriks[0][i] == "X":
                x_loendur += 1
            elif maatriks[0][i] == "O":
                o_loendur += 1
        if maatriks[1][i] == maatriks[2][i] == maatriks[3][i]:
            if maatriks[1][i] == "X":
                x_loendur += 1
            elif maatriks[1][i] == "O":
                o_loendur += 1
    for i in range(1):
        if maatriks[i][i] == maatriks[i+1][i+1] == maatriks[i+2][i+2]:
            if maatriks[i][i] == "X":
                x_loendur += 1
            elif maatriks[i][i] == "O":
                o_loendur += 1
    võitja["X"] = x_loendur
    võitja["O"] = o_loendur
    return võitja