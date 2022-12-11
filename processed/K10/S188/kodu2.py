def võitja(maatriks):
    koguarv_x = 0
    koguarv_o = 0
    for i in range(len(maatriks)):
        for j in range(len(maatriks)):
            if maatriks[i][j] == "X":
                if j < 2:
                    if maatriks[i][j+1] == "X" and maatriks[i][j+2] == "X":
                        koguarv_x += 1
                if i < 2:
                    if maatriks[i+1][j] == "X" and maatriks[i+2][j] == "X":
                        koguarv_x += 1
                if i < 2 and j < 2:
                    if maatriks[i+1][j+1] == "X" and maatriks[i+2][j+2] == "X":
                        koguarv_x += 1
                if i < 2 and j > 1:
                    if maatriks[i+1][j-1] == "X" and maatriks[i+2][j-2] == "X":
                        koguarv_x += 1
            elif maatriks[i][j] == "O":
                if j < 2:
                    if maatriks[i][j+1] == "O" and maatriks[i][j+2] == "O":
                        koguarv_o += 1
                if i < 2:
                    if maatriks[i+1][j] == "O" and maatriks[i+2][j] == "O":
                        koguarv_o += 1
                if i < 2 and j < 2:
                    if maatriks[i+1][j+1] == "O" and maatriks[i+2][j+2] == "O":
                        koguarv_o += 1
                if i < 2 and j > 1:
                    if maatriks[i+1][j-1] == "O" and maatriks[i+2][j-2] == "O":
                        koguarv_o += 1
    andmed = {}
    andmed["O"] = koguarv_o
    andmed["X"] = koguarv_x
    return andmed
