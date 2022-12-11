def võitja(maatriks):
    sõnastik = {"X":0, "O":0}
    for i in range(4):
        for j in range(2):
            if maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2] == "X": 
                sõnastik["X"] += 1
            elif maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2] == "O":
                sõnastik["O"] += 1
            if maatriks[j][i] == maatriks[j+1][i] == maatriks[j+2][i] == "X": 
                sõnastik["X"] += 1
            elif maatriks[j][i] == maatriks[j+1][i] == maatriks[j+2][i] == "O": 
                sõnastik["O"] += 1
    for i in range(2):
        for j in range(2):
            if maatriks[i][j] == maatriks[i+1][j+1] == maatriks[i+2][j+2] == "X":
                sõnastik["X"] += 1
            elif maatriks[i][j] == maatriks[i+1][j+1] == maatriks[i+2][j+2] == "O":
                sõnastik["O"] += 1
            if maatriks[i][j+2] == maatriks[i+1][j+1] == maatriks[i+2][j] == "X":
                sõnastik["X"] += 1
            elif maatriks[i][j+2] == maatriks[i+1][j+1] == maatriks[i+2][j] == "O":
                sõnastik["O"] += 1
    return sõnastik
