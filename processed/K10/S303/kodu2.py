def võitja(maatriks):
    seis = {'O': 0, 'X': 0}
    for i in range(4):
        for j in range(4):
            if maatriks[i][j] == 'O' or maatriks[i][j] == 'X':
                if not j + 2 >= 4:
                    järjend = [maatriks[i][j], maatriks[i][j+1], maatriks[i][j+2]]
                    if set(järjend) == {'O'} or set(järjend) == {'X'}:
                        seis[maatriks[i][j]] += 1
                        
                if not i + 2 >= 4:
                    järjend = [maatriks[i][j], maatriks[i+1][j], maatriks[i+2][j]]
                    if set(järjend) == {'O'} or set(järjend) == {'X'}:
                        seis[maatriks[i][j]] += 1
                    
                if not j + 2 >= 4 and not i + 2 >= 4:
                    järjend = [maatriks[i][j], maatriks[i+1][j+1], maatriks[i+2][j+2]]
                    if set(järjend) == {'O'} or set(järjend) == {'X'}:
                        seis[maatriks[i][j]] += 1
                
                if not j - 2 < 0 and not i + 2 >= 4:
                    järjend = [maatriks[i][j], maatriks[i+1][j-1], maatriks[i+2][j-2]]
                    if set(järjend) == {'O'} or set(järjend) == {'X'}:
                        seis[maatriks[i][j]] += 1
                
    return seis
