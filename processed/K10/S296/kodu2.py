def võitja(m):
    tulemus = {}
    X = 0
    O = 0
    k = 3
    for i in range(0,2): #veergude kaupa kontroll
        for j in range(0,4):
            if m[i][j] == m[i+1][j] == m[i+2][j]:
                if m[i][j]=="X":
                    X=X+1
                if m[i][j]=="O":
                    O=O+1
    for j in range(0,2): 
        for i in range(0,2): #diagonaalide kontroll vasakult paremale
             if m[i][j] == m[i+1][j+1] == m[i+2][j+2]:
                if m[i][j]=="X":
                    X=X+1
                if m[i][j]=="O":
                    O=O+1
        for k in range(2,4): #diagonaalide kontroll paremalt vasakule
            if m[j][k] == m[j+1][k-1] == m[j+2][k-2]:
                if m[j][k]=="X":
                    X=X+1
                if m[j][k]=="O":
                    O=O+1
        for i in range(0,4): #ridade kaupa kontroll
            if m[i][j] == m[i][j+1] == m[i][j+2]:
                if m[i][j]=="X":
                    X=X+1
                if m[i][j]=="O":
                    O=O+1
                    
    tulemus['X']=X
    tulemus['O']=O
    return tulemus
    
print(võitja([[' ',' ',' ','O'],
            [' ','X','O',' '],
            ['','O','X',''],
            ['','','','X']]))
    
        