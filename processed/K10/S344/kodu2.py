def võitja(maatriks):
    sümbol = 0
    X_arv = 0
    O_arv = 0
    tulemus = {}

    for i in range(len(maatriks)):
        for j in range(len(maatriks[i])):
            if i < 2:
                vert1 = maatriks[i][j]==maatriks[i+1][j]==maatriks[i+2][j]
                if vert1 == True:
                    if maatriks[i][j] == 'X':
                        X_arv += 1
                    if maatriks[i][j] == 'O':
                        O_arv += 1
                #print("vert ", i, " ", j, " ", vert1)

            if j < 2:        
                hor1 = maatriks[i][j]==maatriks[i][j+1]==maatriks[i][j+2]
                if hor1 == True:
                    if maatriks[i][j] == 'X':
                        X_arv += 1
                    if maatriks[i][j] == 'O':
                        O_arv += 1
                #print("hor ", i, " ", j, " ", hor1)
            
            if i < 2 and j < 2:
                diag1 = maatriks[i][j]==maatriks[i+1][j+1]==maatriks[i+2][j+2]
                if diag1 == True:
                    if maatriks[i][j] == 'X':
                        X_arv += 1
                    if maatriks[i][j] == 'O':
                        O_arv += 1
                #print("diag\ ", i, " ", j, " ", diag1)
                        
            if i < 2 and j > 1:
                diag2 = maatriks[i][j]==maatriks[i+1][j-1]==maatriks[i+2][j-2]
                if diag2 == True:
                    if maatriks[i][j] == 'X':
                        X_arv += 1
                    if maatriks[i][j] == 'O':
                        O_arv += 1
                #print("diag/ ", i, " ", j, " ", diag2)
            
    tulemus["O"] = O_arv
    tulemus["X"] = X_arv
    return tulemus
            
    
print(võitja([[' ',' ',' ',' '],
              [' ',' ',' ',' '],
              [' ',' ',' ',' '],
              [' ',' ',' ',' ']])) 