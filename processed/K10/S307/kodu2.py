def võitja(a):
    X = 0
    O = 0
    tulemus = {}
    
    ##DIAGONAAL PAREMALE
    for i in range(0,2):
        for j in range(0,2):
            if a[i][j] == a[i+1][j+1] == a[i+2][j+2] == 'X':
                X+=1
    for i in range(0,2):
        for j in range(0,2):
            if a[i][j] == a[i+1][j+1] == a[i+2][j+2] == 'O':
                O+=1
    ##DIAGONAAL VASAKULE
    for i in range(2, 4):
        for j in range(2):
            if a[i][j] == a[i-1][j+1] == a[i-2][j+2] ==  'X':
                X+=1
    for i in range(2, 4):
        for j in range(2):
            if a[i][j] == a[i-1][j+1] == a[i-2][j+2] == 'O':
                O+=1
    ##VEERUD
    for i in range(2):
        for j in range(4):
            if a[i][j] == a[i+1][j] == a[i+2][j] == 'X':
                X+=1
    for i in range(2):
        for j in range(4):
            if a[i][j] == a[i+1][j] == a[i+2][j] == 'O':
                O+=1
    ##READ
    for i in range(4):
        for j in range(2):
            if a[i][j] == a[i][j+1] == a[i][j+2] == 'X':
                X+=1
    for i in range(4):
        for j in range(2):
            if a[i][j] == a[i][j+1] == a[i][j+2] == 'O':
                O+=1
        
    
    tulemus['X'] = X
    tulemus['O'] = O
    return tulemus

