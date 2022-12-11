def võitja(maatriks):
    loendur = {}
    x = 0
    o = 0
    for i in range(len(maatriks)):
        for j in range(2):
            if maatriks[i][j] == "X" and maatriks[i][j+1] == "X" and maatriks[i][j+2] == "X":
                x += 1
    for i in range(len(maatriks)):
        for j in range(2):        
            if maatriks[i][j] == "O" and maatriks[i][j+1] == "O" and maatriks[i][j+2] == "O":
                o += 1
    for i in range(2):
        for j in range(4):
            if maatriks[i][j] == "X" and maatriks[i+1][j] == "X" and maatriks[i+2][j] == "X":
                x += 1
    for i in range(2):
        for j in range(4):
            if maatriks[i][j] == "O" and maatriks[i+1][j] == "O" and maatriks[i+2][j] == "O":
                o += 1
    for i in range(2):
        for j in range(2):
            if maatriks[i][j] == "X" and maatriks[i+1][j+1] == "X" and maatriks[i+2][j+2] == "X":
                x += 1
    for i in range(2):
        for j in range(2):
            if maatriks[i][j] == "O" and maatriks[i+1][j+1] == "O" and maatriks[i+2][j+2] == "O":
                o += 1
    for i in range(2):
        for j in range(2):
            if maatriks[i][j+2] == "O" and maatriks[i+1][j+1] == "O" and maatriks[i+2][j] == "O":
                o += 1
    for i in range(2):
        for j in range(2):
            if maatriks[i][j+2] == "X" and maatriks[i+1][j+1] == "X" and maatriks[i+2][j] == "X":
                x += 1
    loendur["X"] = x
    loendur["O"] = o
                  
    return loendur