def võitja(maatriks):
    sõnastik = {}
    x_lugeja = 0
    o_lugeja = 0
    for i in range(4):
        for j in range(2):
            if maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2] == "X":
                x_lugeja += 1
            elif maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2] == "O":
                o_lugeja += 1
    for i in range(2):
        for j in range(4):
            if maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j] == "X":
                x_lugeja += 1
            elif maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j] == "O":
                o_lugeja += 1
    for i in range(2):
        for j in range(2):
            if maatriks[i][j] == maatriks[i+1][j+1] == maatriks[i+2][j+2] == "X":
                x_lugeja += 1
            elif maatriks [i][j] == maatriks[i+1][j+1] == maatriks[i+2][j+2] == "O":
                o_lugeja += 1
    for i in range(2):
        for j in range(3,1,-1):
            if maatriks[i][j] == maatriks[i+1][j-1] == maatriks[i+2][j-2] == "X":
                x_lugeja += 1
            elif maatriks[i][j] == maatriks[i+1][j-1] == maatriks[i+2][j-2] == "O":
                o_lugeja += 1
    sõnastik["X"] = x_lugeja
    sõnastik["O"] = o_lugeja
    return sõnastik

maatriks =([["O","O","O","X"],
            ["O","O","X","X"],
            ["O","X","O"," "],
            ["X","X","X","O"]])

print(võitja(maatriks))
            