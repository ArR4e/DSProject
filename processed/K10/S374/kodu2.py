def võitja(maatriks):
    sonastik = {'O': 0, 'X': 0}
    
    for rida in maatriks:
       for i in range(2):
            if rida[i] == 'X' and rida[i+1] == 'X' and rida[i+2] == 'X':
               sonastik['X'] += 1
            elif rida[i] == 'O' and rida[i+1] == 'O' and rida[i+2] == 'O':
               sonastik['O'] += 1
            
    for i in range(2):
        for j in range(4):
                if maatriks[i][j] == 'X' and maatriks[i+1][j] == 'X' and maatriks[i+2][j] == 'X':
                   sonastik['X'] += 1
                elif maatriks[i][j] == 'O' and maatriks[i+1][j] == 'O' and maatriks[i+2][j] == 'O':
                   sonastik['O'] += 1
                   
    for i in range(2):
        for j in range(2):
            if maatriks[i][j] == 'X' and maatriks[i+1][j+1] == 'X' and maatriks[i+2][j+2] == 'X':
                sonastik['X'] += 1
            elif maatriks[i][j] == 'O' and maatriks[i+1][j+1] == 'O' and maatriks[i+2][j+2] == 'O':
                sonastik['O'] += 1
                
    for i in range(2):
        for j in range(-2,0):
            if maatriks[i][j] == 'X' and maatriks[i+1][j-1] == 'X' and maatriks[i+2][j-2] == 'X':
                sonastik['X'] += 1
            elif maatriks[i][j] == 'O' and maatriks[i+1][j-1] == 'O' and maatriks[i+2][j-2] == 'O':
                sonastik['O'] += 1

    
             
    return sonastik