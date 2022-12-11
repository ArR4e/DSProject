def võitja(maatriks):
    xv = 0
    ov = 0
    for el in maatriks:
        if el[0] == "O" and el[1] == "O" and el[2] == "O":
            ov += 1
        if el[1] == "O" and el[2] == "O" and el[3] == "O":
            ov += 1
        if el[0] == "X" and el[1] == "X" and el[2] == "X":
            xv += 1
        if el[1] == "X" and el[2] == "X" and el[3] == "X":
            xv += 1
    for i in (0,1):
        for j in range(4):
            if maatriks[i][j] == "O" and maatriks[i+1][j] == "O" and maatriks[i+2][j] == "O":
                ov += 1
            if maatriks[i][j] == "X" and maatriks[i+1][j] == "X" and maatriks[i+2][j] == "X":
                xv += 1
    for i in (0,1):
        for j in (0,1):
            if maatriks[i][j] == "O" and maatriks[i+1][j+1] == "O" and maatriks[i+2][j+2] == "O":
                ov += 1
            if maatriks[i][j] == "X" and maatriks[i+1][j+1] == "X" and maatriks[i+2][j+2] == "X":
                xv += 1
            if maatriks[i][j+2] == "O" and maatriks[i+1][j+1] == "O" and maatriks[i+2][j] == "O":
                ov += 1
            if maatriks[i][j+2] == "X" and maatriks[i+1][j+1] == "X" and maatriks[i+2][j] == "X":
                xv += 1
    tekst = {}
    tekst["O"] = ov
    tekst["X"] = xv
    return tekst

maatriks = [[' ', 'X', ' ', 'O'],
            [' ', 'X', ' ', 'O'],
            [' ', 'X', ' ', 'O'],
            [' ', ' ', ' ', ' ']]
print(võitja(maatriks))