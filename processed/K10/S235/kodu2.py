def võitja(maatriks):
    sõnastik = {}
    sõnastik["X"] = read(maatriks, "X") + veerud(maatriks, "X") + diagonaalid(maatriks, "X")
    sõnastik["O"] = read(maatriks, "O") + veerud(maatriks, "O") + diagonaalid(maatriks, "O")
    return sõnastik

def read(maatriks, sümbol):
    arv = 0
    for i in range(len(maatriks)):
        for j in range(len(maatriks[0])-2):
            if maatriks[i][j:j+3].count(sümbol) == 3:
                arv += 1
    return arv

def veerud(maatriks, sümbol):
    arv = 0
    for i in range(len(maatriks)-2):
        for j in range(len(maatriks[0])):
            if maatriks[i][j] == sümbol and maatriks[i+1][j] == sümbol and maatriks[i+2][j] == sümbol:
                arv += 1
    return arv

def diagonaalid(maatriks, sümbol):
    arv = 0
    for i in range(len(maatriks)-2):
        for j in range(len(maatriks[0])-2):
            if maatriks[i][j] == sümbol and maatriks[i+1][j+1] == sümbol and maatriks[i+2][j+2] == sümbol:
                arv += 1
    for i in range(len(maatriks)-2):
        for j in range(2, len(maatriks[0])):
            if maatriks[i][j] == sümbol and maatriks[i+1][j-1] == sümbol and maatriks[i+2][j-2] == sümbol:
                arv += 1
    return arv

