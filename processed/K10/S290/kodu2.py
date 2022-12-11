def võitja(maatriks):
    X = 0
    O = 0
    for i in range(4):
        for j in range(2):
            if maatriks[i][j]==maatriks[i][j+1]==maatriks[i][j+2]:
                if maatriks[i][j+1] == "X":
                    X += 1
                if maatriks[i][j+1] == "O":
                    O += 1
    for i in range(2):
        for j in range(4):
            if maatriks[i][j]==maatriks[i+1][j]==maatriks[i+2][j]:
                if maatriks[i+1][j] == "X":
                    X += 1
                if maatriks[i+1][j] == "O":
                    O += 1
    for i in range(2):
        if maatriks[i][i]==maatriks[i+1][i+1]==maatriks[i+2][i+2]:
            if maatriks[i+1][i+1] == "X":
                X += 1
            if maatriks[i+1][i+1] == "O":
                O += 1
    for i in range(2):
        if maatriks[i][i+2]==maatriks[i+1][i+1]==maatriks[i+2][i]:
            if maatriks[i+1][i+1] == "X":
                X += 1
            if maatriks[i+1][i+1] == "O":
                O += 1

    s = {}
    s["X"]=X
    s["O"]=O
            
    return(s)

kolm =võitja([['O',' ','O','X'],
            ['O','O','X','X'],
            ['O','X','O',' '],
            ['X','X','X','O']])
print(kolm)
    