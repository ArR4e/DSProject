def võitja(maatriks):
    sõnastik = {}
    o = 0
    x = 0
    
    for i in range(len(maatriks)):
        for j in range(2):
            if maatriks[i][j] == "O" and maatriks[i][j+1] == "O" and maatriks[i][j+2] == "O":
                o += 1
            elif maatriks[i][j] == "X" and maatriks[i][j+1] == "X" and maatriks[i][j+2] == "X":
                x += 1
            else:
                continue
            
    for i in range(2):
        for j in range(len(maatriks[i])):
            if maatriks[i][j] == "O" and maatriks[i+1][j] == "O" and maatriks[i+2][j] == "O":
                o += 1
            elif maatriks[i][j] == "X" and maatriks[i+1][j] == "X" and maatriks[i+2][j] == "X":
                x += 1
            else:
                continue
            
    for i in range(2):
        for j in range(2):
            if maatriks[i][j] == "O" and maatriks[i+1][j+1] == "O" and maatriks[i+2][j+2] == "O":
                o += 1
            elif maatriks[i][j] == "X" and maatriks[i+1][j+1] == "X" and maatriks[i+2][j+2] == "X":
                x += 1
            else:
                continue
    
    for i in range(1, 3):
        for j in range(2):
            if maatriks[i*(-1)][j] == "O" and maatriks[(i+1)*(-1)][j+1] == "O" and maatriks[(i+2)*(-1)][j+2] == "O":
                o += 1
            elif maatriks[i*(-1)][j] == "X" and maatriks[(i+1)*(-1)][j+1] == "X" and maatriks[(i+2)*(-1)][j+2] == "X":
                x += 1
            else:
                continue

    sõnastik["O"] = o
    sõnastik["X"] = x
    
    return sõnastik