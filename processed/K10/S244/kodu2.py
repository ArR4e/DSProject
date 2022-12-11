def võitja(maatriks):
    sõnastik = {}
    X = 0
    O = 0
    for i in range(4):
        for j in range(2):
            if maatriks[i][j]==maatriks[i][j+1]==maatriks[i][j+2]== 'X':
                X += 1
            if maatriks[i][j]==maatriks[i][j+1]==maatriks[i][j+2]== 'O':
                O += 1
    for i in range(2):
        for j in range(4):
            if maatriks[i][j]==maatriks[i+1][j]==maatriks[i+2][j]== 'X':
                X += 1
            if maatriks[i][j]==maatriks[i+1][j]==maatriks[i+2][j]== 'O':
                O += 1
    for i in range(2):
        for j in range(2):
            if maatriks[i][j]==maatriks[i+1][j+1]==maatriks[i+2][j+2] == 'X':
                X+=1
            if maatriks[i][j]==maatriks[i+1][j+1]==maatriks[i+2][j+2] == 'O':
                O+=1
    for i in range(2):
        for j in range(2):
            if maatriks[i][j+2] == maatriks[i+1][j+1] == maatriks[i+2][j] == 'X':
                X+=1
            if maatriks[i][j+2] == maatriks[i+1][j+1] == maatriks[i+2][j] == 'O':
                O+=1
    
    sõnastik['X'] = X
    sõnastik['O'] = O
    return sõnastik
            
            


maatriks = (['X', 'X', 'O', 'O'], ['O', 'O', 'X', 'X'], ['X', 'X', 'O', 'O'], ['O', 'O', 'X', 'X'])
print(võitja(maatriks))