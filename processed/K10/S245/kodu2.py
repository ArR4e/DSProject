maatriks = ([[' ',' ',' ',' '],
       [' ',' ',' ',' '],
       [' ',' ',' ',' '],
       [' ',' ',' ',' ']])

X_loendur = 0
O_loendur = 0
def võitja(maatriks):
    if maatriks == "X":
        X_loendur += 1
    for i in range(2):
        for j in range(2):
            print(maatriks[i][j]+maatriks [i][j+1]+maatriks[i][j+2])
    print(X_loendur)     
    
võitja(maatriks)