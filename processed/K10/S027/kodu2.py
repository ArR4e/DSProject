def võitja(maatriks):
    võidud = {}
    X_võit = 0
    O_võit = 0
    for rida in range(len(maatriks)):
        for arv in range(len(maatriks[rida])):
            if arv+2 <= 3:
                if maatriks[rida][arv] == maatriks[rida][arv+1] == maatriks[rida][arv+2] == 'X':
                    X_võit += 1
                if maatriks[rida][arv] == maatriks[rida][arv+1] == maatriks[rida][arv+2] == 'O':
                    O_võit +=1
            
            if rida+2 <= 3:
                if maatriks[rida][arv] == maatriks[rida+1][arv] == maatriks[rida+2][arv] == 'X':
                    X_võit += 1
                if maatriks[rida][arv] == maatriks[rida+1][arv] == maatriks[rida+2][arv] == 'O':
                    O_võit += 1
                    
                    
            if rida+2 <= 3 and arv+2 <= 3:
                if maatriks[rida][arv] == maatriks[rida+1][arv+1] == maatriks[rida+2][arv+2] == 'X':
                    X_võit += 1
                if maatriks[rida][arv] == maatriks[rida+1][arv+1] == maatriks[rida+2][arv+2] == 'O':
                    O_võit +=1
                    
            if rida+2 <= 3 and arv-2 >= 0:
                if maatriks[rida][arv] == maatriks[rida+1][arv-1] == maatriks[rida+2][arv-2] == 'X':
                    X_võit += 1
                if maatriks[rida][arv] == maatriks[rida+1][arv-1] == maatriks[rida+2][arv-2] == 'O':
                    O_võit +=1
                    
    võidud['X'] = X_võit
    võidud['O'] = O_võit
    return võidud




print(võitja([['O','','O','X'],
            ['O','O','X','X'],
            ['O','X','O',''],
            ['X','X','X','O']]))