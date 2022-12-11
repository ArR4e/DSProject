def võitja(maatriks):
    X_arv = 0
    O_arv = 0
    
    for i in range(len(maatriks)):
        for j in range(len(maatriks[i])):
            if "X" == maatriks[i][j]:
                if j <= 1:
                    #esimese rea elemendid
                    if "X" == maatriks[i][j+1] and "X" == maatriks[i][j+2]:
                        X_arv += 1
                if i <= 1:
                    if "X" == maatriks[i+1][j] and "X" == maatriks[i+2][j]:
                        X_arv += 1
                if j <= 1 and i <= 1:
                    if "X" == maatriks[i+1][j+1] and "X" == maatriks[i+2][j+2]:
                        X_arv += 1
                if j >= 2 and i <=1:
                    if "X" == maatriks[i+1][j-1] and "X" == maatriks[i+2][j-2]:
                        X_arv += 1
            if "O" == maatriks[i][j]:
                if j <= 1:
                    if "O" == maatriks[i][j+1] and "O" == maatriks[i][j+2]:
                        O_arv += 1
                if i <= 1:
                    if "O" == maatriks[i+1][j] and "O" == maatriks[i+2][j]:
                        O_arv += 1
                if j <= 1 and i <= 1:
                    if "O" == maatriks[i+1][j+1] and "O" == maatriks[i+2][j+2]:
                        O_arv += 1
                if j >= 2 and i <= 1:
                    if "O" == maatriks[i+1][j-1] and "O" == maatriks[i+2][j-2]:
                        O_arv += 1
    sõnastik = {"X": X_arv, "O": O_arv}
    return sõnastik
print(võitja([[' ',' ',' ',' '],
            ['O',' ',' ',' '],
            ['O',' ',' ',' '],
            ['O','X','X','X']])
      )
