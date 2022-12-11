def võitja(maatriks):
    sõnastik = {}
    X_kokku = 0
    O_kokku = 0
    for i in range(4):
        for j in range(2):
            #kontrollib ridu
            if maatriks[i][j] == "X" and maatriks[i][j+1] == "X" and maatriks[i][j+2] == "X":
                X_kokku +=1
            elif maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2] == "O":
                O_kokku +=1
            #kontrollib veerge
            if maatriks[j][i] == "X" and maatriks[j+1][i] == "X" and maatriks[j+2][i] == "X":
                X_kokku +=1
            elif maatriks[j][i] == maatriks[j+1][i] == maatriks[j+2][i] == "O":
                O_kokku +=1
    for i in range(2):
        for j in range(2):
            #diagonaal1
            if maatriks[i][j] == maatriks[i+1][j+1] == maatriks[i+2][j+2] == "O":
                O_kokku +=1
            elif maatriks[i][j] == maatriks[i+1][j+1] == maatriks[i+2][j+2] == "X":
                X_kokku +=1
    for i in range(2,4):
        for j in range(2):
            #diagonaal2
            if maatriks[i][j] == maatriks[i-1][j+1] == maatriks[i-2][j+2] == "O":
                O_kokku +=1
            elif maatriks[i][j] == maatriks[i-1][j+1] == maatriks[i-2][j+2] == "X":
                X_kokku +=1  
                
    sõnastik["X"] = X_kokku
    sõnastik["O"] = O_kokku
    return sõnastik

print(võitja([['O',' ','O','X'],
            ['O','O','X','X'],
            ['O','X','O',' '],
            ['X','X','X','O']]))
    