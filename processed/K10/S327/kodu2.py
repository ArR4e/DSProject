def võitja(maatriks):
    X_arv = 0
    O_arv = 0
    a = ""
    X_võidud = [" XXX", "XXX ", "OXXX", "XXXO", "XXX"]
    O_võidud = [" OOO", "OOO ", "XOOO", "OOOX", "OOO"]
    tulemus = {}
    
    for i in range(0,4):
        for j in range(0,4):
            a += maatriks[i][j]
        if a == "XXXX":
            X_arv += 2
        elif a in X_võidud:
            X_arv += 1
        if a == "OOOO":
            O_arv += 2
        elif a in O_võidud:
            O_arv += 1
        a = ""
        
    for i in range(0,4):
        for j in range(0,4):
            a += maatriks[j][i]
        if a == "XXXX":
            X_arv += 2
        elif a in X_võidud:
            X_arv += 1
        if a == "OOOO":
            O_arv += 2
        elif a in O_võidud:
            O_arv += 1
        a = ""
        
    for x in range(0,4):
        for y in range(0,4):
            a += maatriks[y][x]
            
            if len(maatriks) >= (1+y)+2 and len(maatriks[y]) >= (1+x)+2:
                a = maatriks[y][x] + maatriks[y+1][x+1] + maatriks[y+2][x+2]
                
                if a in X_võidud:
                    X_arv += 1
                elif a in O_võidud:
                    O_arv += 1
                a = ""
                
            else:
                a = ""
                
    for x in range(0, 4):
        for y in range(0, 4):
            a += maatriks[y][x]
            
            if len(maatriks) >= (1+y)+2 and x-2 >= 0:
                a = maatriks[y][x] + maatriks[y+1][x-1] + maatriks[y+2][x-2]
                
                if a in X_võidud:
                    X_arv += 1
                elif a in O_võidud:
                    O_arv += 1
                a = ""
                
            else:
                a = ""
                
    tulemus['X'] = X_arv
    tulemus['O'] = O_arv
    
    return tulemus
print(võitja([['X','X','X','X'],
            ['O','O','O','X'],
            ['O','O','O','X'],
            ['O',' ',' ','O']]))
