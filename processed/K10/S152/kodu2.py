#read, veerud
def võitja(maatriks):
    x_loendur = 0
    o_loendur = 0
    tühi = 0
    sõnastik = {}
    for i in range(4):
        for j in range(2):
            a = maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2]
            if a == True:
                sümbol = maatriks[i][j]
                if sümbol == "X":
                    x_loendur += 1
                elif sümbol == "O":
                    o_loendur += 1
                else:
                    tühi += 1
                    
    for i in range(2):
        for j in range(4):
            a = maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j]
            if a == True:
                sümbol = maatriks[i][j]
                if sümbol == "X":
                    x_loendur += 1
                elif sümbol == "O":
                    o_loendur += 1
                else:
                    tühi += 1
                    
    for i in range(2):
        for j in range(2):
            b = maatriks[i][j] == maatriks[i+1][j+1] == maatriks[i+2][j+2]
            if b == True:
                sümbol = maatriks[i][j]
                if sümbol == "X":
                    x_loendur += 1
                elif sümbol == "O":
                    o_loendur += 1
                else:
                    tühi += 1
                    
    for i in range(2):
        for j in range(2,4):
            b = maatriks[i][j] == maatriks[i+1][j-1] == maatriks[i+2][j-2]
            if b == True:
                sümbol = maatriks[i][j]
                if sümbol == "X":
                    x_loendur += 1
                elif sümbol == "O":
                    o_loendur += 1
                else:
                    tühi += 1
                    
    sõnastik["X"] = x_loendur
    sõnastik["O"] = o_loendur
    
    return sõnastik

            