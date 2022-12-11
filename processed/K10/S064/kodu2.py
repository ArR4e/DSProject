# 2. Trips-traps-trull

def võitja(maatriks):
    sõnastik = {}
    X_punktid = 0
    O_punktid = 0
    # HORISONTAALSELT
    for el in range(4):
        for j in range(2):
            if maatriks[el][j] == maatriks[el][j + 1] == maatriks[el][j + 2] == "O":
                O_punktid += 1
            elif maatriks[el][j] == maatriks[el][j + 1] == maatriks[el][j + 2] == "X":
                X_punktid += 1
            elif maatriks[el][0] == maatriks[el][1] == maatriks[el][2] == maatriks[el][3] == "O":
                O_punktid += 2
            elif maatriks[el][0] == maatriks[el][1] == maatriks[el][2] == maatriks[el][3] == "X":
                X_punktid += 2
        
    # VERTIKAALSELT
    for el in range(2):
        for j in range(4):
            if maatriks[el][j] == maatriks[el+1][j] == maatriks[el+2][j] == "O":
                O_punktid += 1
            elif maatriks[el][j] == maatriks[el+1][j] == maatriks[el+2][j] == "X":
                X_punktid += 1
            elif maatriks[0][j] == maatriks[1][j] == maatriks[2][j] == maatriks[3][j] == "O":
                O_punktid += 2
            elif maatriks[0][j] == maatriks[1][j] == maatriks[2][j] == maatriks[3][j] == "X":
                X_punktid += 2
                
    # PEADIAGONAALIL
    for el in range(2):
        for j in range(2):
            if maatriks[el][j] == maatriks[el+1][j+1] == maatriks[el+2][j+2] == "O":
                O_punktid += 1
            elif maatriks[el][j] == maatriks[el+1][j+1] == maatriks[el+2][j+2] == "X":
                X_punktid += 1
    for el in range(0):
        for j in range(0):
            if maatriks[el][j] == maatriks[el+1][j+1] == maatriks[el+2][j+2] == maatriks[el+3][j+3] == "O":
                O_punktid += 2
            elif maatriks[el][j] == maatriks[el+1][j+1] == maatriks[el+2][j+2] == maatriks[el+3][j+3] == "X":
                X_punktid += 2
            
    # KÕRVALDIAGONAALIL
    for el in range(2):
        for j in range(2):
            if maatriks[el][j+2] == maatriks[el+1][j+1] == maatriks[el+2][j] == "O":
                O_punktid += 1
            elif maatriks[el][j+2] == maatriks[el+1][j+1] == maatriks[el+2][j] == "X":
                X_punktid += 1
    for el in range(0):
        for j in range(0):
            if maatriks[el][j+3] == maatriks[el+1][j+2] == maatriks[el+2][j+1] == maatriks[el+3][j] == "O":
                O_punktid += 2
            elif maatriks[el][j+3] == maatriks[el+1][j+2] == maatriks[el+2][j+1] == maatriks[el+3][j] == "X":
                X_punktid += 2
                
    sõnastik["O"] = O_punktid
    sõnastik["X"] = X_punktid
    return sõnastik

maatriks = [["O", " ", "O", "X"],
            ["O", "O", "X", "X"],
            ["O", "X", "O", " "],
            ["X", "X", "X", "O"]]

võitja(maatriks)