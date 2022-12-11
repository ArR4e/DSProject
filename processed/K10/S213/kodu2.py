def võitja(maatriks):
    
    mangjadList =['O', 'X']
    
    sonastikMaatriks = {}
    
    for el in mangjadList:
        
        value = 0

        for i in range(0, 4):
            if maatriks[i][0]  == el and maatriks[i][1]  == el and maatriks[i][2] == el:
                value += 1
            if maatriks[i][1]  == el and maatriks[i][2]  == el and maatriks[i][3] == el:
                value += 1
                
        if maatriks[1][0] == el and maatriks[2][1] == el and maatriks[3][2] == el:
            value += 1
        if maatriks[0][0] == el and maatriks[1][1] == el and maatriks[2][2] == el:
            value += 1
        if maatriks[1][1] == el and maatriks[2][2] == el and maatriks[3][3] == el:
            value += 1
        if maatriks[0][1] == el and maatriks[1][2] == el and maatriks[2][3] == el:
            value += 1

        if maatriks[0][2] == el and maatriks[1][1] == el and maatriks[2][0] == el:
            value += 1
        if maatriks[0][3] == el and maatriks[1][2] == el and maatriks[2][1] == el:
            value += 1
        if maatriks[1][2] == el and maatriks[2][1] == el and maatriks[3][0] == el:
            value += 1
        if maatriks[1][3] == el and maatriks[2][2] == el and maatriks[3][1] == el:
            value += 1
        
        
        
        for i in range(0, 4):
            if maatriks[0][i] == el and maatriks[1][i] == el and maatriks[2][i] == el:
                value += 1
            if maatriks[1][i] == el and maatriks[2][i] == el and maatriks[3][i] == el:
                value += 1
        
        
        sonastikMaatriks[el] = value
    
    return sonastikMaatriks

print(võitja([['O',' ','O','X'],
            ['O','O','X','X'],
            ['O','X','O',' '],
            ['X','X','X','O']]))
