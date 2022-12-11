
def võitja(maatriks):
    Xloendur = 0
    Oloendur = 0
    sõnastik = {}
    sõnastik["X"] = Xloendur
    sõnastik["O"] = Oloendur
    for i in range(4):
        for j in range(2):
            sümbolkogu = maatriks[i][j]+maatriks[i][j+1]+maatriks[i][j+2]
            if sümbolkogu == "XXX":
                Xloendur += 1
                sõnastik["X"] = Xloendur
            if sümbolkogu == "OOO":
                Oloendur += 1
                sõnastik["O"] = Oloendur
    for i in range(2):
        for j in range(4):
            sümbolkogu = maatriks[i][j]+maatriks[i+1][j]+maatriks[i+2][j]
            if sümbolkogu == "XXX":
                Xloendur += 1
                sõnastik["X"] = Xloendur
            if sümbolkogu == "OOO":
                Oloendur += 1
                sõnastik["O"] = Oloendur
    for i in range(1):
        for j in range(1):
            sümbolkogu = maatriks[i][j]+maatriks[i+1][j+1]+maatriks[i+2][j+2]
            if sümbolkogu == "XXX":
                Xloendur += 1
                sõnastik["X"] = Xloendur
            if sümbolkogu == "OOO":
                Oloendur += 1
                sõnastik["O"] = Oloendur
    for i in range(1):
        for j in range(1):
            sümbolkogu = maatriks[i+1][j+1]+maatriks[i+2][j+2]+maatriks[i+3][j+3]
            if sümbolkogu == "XXX":
                Xloendur += 1
                sõnastik["X"] = Xloendur
            if sümbolkogu == "OOO":
                Oloendur += 1
                sõnastik["O"] = Oloendur
    for i in range(1):
        for j in range(1):
            sümbolkogu = maatriks[i][j+3]+maatriks[i+1][j+2]+maatriks[i+2][j+1]
            if sümbolkogu == "XXX":
                Xloendur += 1
                sõnastik["X"] = Xloendur
            if sümbolkogu == "OOO":
                Oloendur += 1
                sõnastik["O"] = Oloendur
    for i in range(1):
        for j in range(1):
            sümbolkogu = maatriks[i+1][j+2]+maatriks[i+2][j+1]+maatriks[i+3][j]
            if sümbolkogu == "XXX":
                Xloendur += 1
                sõnastik["X"] = Xloendur
            if sümbolkogu == "OOO":
                Oloendur += 1
                sõnastik["O"] = Oloendur
    for i in range(1):
        for j in range(1):
            sümbolkogu = maatriks[i+1][j]+maatriks[i+2][j+1]+maatriks[i+3][j+2]
            if sümbolkogu == "XXX":
                Xloendur += 1
                sõnastik["X"] = Xloendur
            if sümbolkogu == "OOO":
                Oloendur += 1
                sõnastik["O"] = Oloendur
    for i in range(1):
        for j in range(1):
            sümbolkogu = maatriks[i][j+1]+maatriks[i+1][j+2]+maatriks[i+2][j+3]
            if sümbolkogu == "XXX":
                Xloendur += 1
                sõnastik["X"] = Xloendur
            if sümbolkogu == "OOO":
                Oloendur += 1
                sõnastik["O"] = Oloendur
    for i in range(1):
        for j in range(1):
            sümbolkogu = maatriks[i][j+2]+maatriks[i+1][j+1]+maatriks[i+2][j]
            if sümbolkogu == "XXX":
                Xloendur += 1
                sõnastik["X"] = Xloendur
            if sümbolkogu == "OOO":
                Oloendur += 1
                sõnastik["O"] = Oloendur
    for i in range(1):
        for j in range(1):
            sümbolkogu = maatriks[i+1][j+3]+maatriks[i+2][j+2]+maatriks[i+3][j+1]
            if sümbolkogu == "XXX":
                Xloendur += 1
                sõnastik["X"] = Xloendur
            if sümbolkogu == "OOO":
                Oloendur += 1
                sõnastik["O"] = Oloendur


    return sõnastik
print(võitja([['O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O']]))