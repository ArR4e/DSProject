def võitja(maatriks):
    seis = {}
    seis['O'] = 0
    seis['X'] = 0
    #kontrollin ridu
    indeks = [range(0,3), range(1,4)]
    for rida in maatriks:
        for n in indeks:
            X=0; O=0
            for i in n:
                if rida[i] == 'X': X += 1
                elif rida[i] == 'O': O += 1
            if X == 3: seis['X'] += 1
            if O == 3: seis['O'] += 1
            
    #kontrollin veerge
    for veerg in list(zip(*maatriks)):       
        for n in indeks:
            X=0; O=0
            for i in n:
                if veerg[i] == 'X': X += 1
                elif veerg[i] == 'O': O += 1
            if X == 3: seis['X'] += 1
            if O == 3: seis['O'] += 1
            
    #kontrolli diagonaale
    for i in range(len(maatriks)):
        for j in range(len(maatriks[i])):
            if maatriks[i][j] == ' ':
                continue
            if i<=1:
                if j<=1:
                    if maatriks[i][j] == maatriks[i+1][j+1] and maatriks[i+1][j+1] == maatriks[i+2][j+2]:
                        seis[maatriks[i][j]] += 1
                else:
                    if maatriks[i][j] == maatriks[i+1][j-1] and maatriks[i+1][j-1] == maatriks[i+2][j-2]:
                        seis[maatriks[i][j]] += 1                    

          
    print(seis)        
    return seis
    

võitja([['O',' ','O','X'],
            ['O','O','X','X'],
            ['O','X','O',' '],
            ['X','X','X','O']])
   
