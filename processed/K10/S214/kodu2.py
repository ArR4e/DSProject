def võitja(maatriks):
    sõnastik = {}
    sõnastik["O"] = 0
    sõnastik["X"] = 0
    #read
    for i in range(4):
        for j in range(2):
            rida = maatriks[i][j]+maatriks[i][j+1]+maatriks[i][j+2]
            if "XXX" in rida:
                sõnastik["X"] = sõnastik.get("X",0) + 1
            elif "OOO" in rida:
                sõnastik["O"] = sõnastik.get("O",0) + 1
    #veerud
    for i in range(2):
        for j in range(4):
            veerg = maatriks[i][j]+maatriks[i+1][j]+maatriks[i+2][j]
            if "XXX" in veerg:
                sõnastik["X"] = sõnastik.get("X",0) + 1
            elif "OOO" in veerg:
                sõnastik["O"] = sõnastik.get("O",0) +1
    #diagonaalid
    for i in range(2):
        for j in range(2):
            diagonaal1 = maatriks[i][j]+maatriks[i+1][j+1]+maatriks[i+2][j+2]
            diagonaal2 = maatriks[i][j+2]+maatriks[i+1][j+1]+maatriks[i+2][j]
            if "XXX" in diagonaal1:
                sõnastik["X"] = sõnastik.get("X",0) + 1
            if "OOO" in diagonaal1:
                sõnastik["O"] = sõnastik.get("O",0) + 1
            if "XXX" in diagonaal2:
                sõnastik["X"] = sõnastik.get("X",0) + 1
            if "OOO" in diagonaal2:
                sõnastik["O"] = sõnastik.get("O",0) + 1
    return sõnastik