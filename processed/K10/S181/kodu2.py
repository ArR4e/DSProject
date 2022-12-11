def võitja(maatriks):
    sõnastik = {"O":0,"X":0}
    for i in range(4):
        for j in range(2):
            if ("XXX" in maatriks[i][j]+maatriks[i][j+1]+maatriks[i][j+2]):
                sõnastik["X"] = sõnastik["X"]+1
            elif ("OOO" in maatriks[i][j]+maatriks[i][j+1]+maatriks[i][j+2]):
                sõnastik["O"] = sõnastik["O"]+1
    for i in range(2):
        for j in range(4):
            if ("XXX" in maatriks[i][j]+maatriks[i+1][j]+maatriks[i+2][j]):
                sõnastik["X"] = sõnastik["X"]+1
            elif ("OOO" in maatriks[i][j]+maatriks[i+1][j]+maatriks[i+2][j]):
                sõnastik["O"] = sõnastik["O"]+1
    for i in range(2):
        for j in range(2):
            if ("XXX" in maatriks[i][j]+maatriks[i+1][j+1]+maatriks[i+2][j+2]):
                sõnastik["X"] = sõnastik["X"]+1
            elif ("OOO" in maatriks[i][j]+maatriks[i+1][j+1]+maatriks[i+2][j+2]):
                sõnastik["O"] = sõnastik["O"]+1
    for i in range(2):
        for j in range(2):
            if ("XXX" in maatriks[i][j+2]+maatriks[i+1][j+1]+maatriks[i+2][j]):
                sõnastik["X"] = sõnastik["X"]+1
            elif ("OOO" in maatriks[i][j+2]+maatriks[i+1][j+1]+maatriks[i+2][j]):
                sõnastik["O"] = sõnastik["O"]+1
    return sõnastik
            