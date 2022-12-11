def kontrolli_diagonaali(tulemus, maatriks, n, offset1, offset2):
    diagonaal_count = 0
    viimane_sümbol = None
    for i in range(n):
        if diagonaal_count >= 3:
            tulemus[viimane_sümbol] += 1
        if maatriks[i + offset1][i + offset2] == viimane_sümbol:
            diagonaal_count += 1
        elif maatriks[i + offset1][i + offset2] != ' ':
            diagonaal_count = 1
            viimane_sümbol = maatriks[i + offset1][i + offset2]
        else:
            diagonaal_count = 0
            viimane_sümbol = None
            
    if diagonaal_count >= 3:
        tulemus[viimane_sümbol] += 1

def võitja(maatriks):
    tulemus = {'O': 0, 'X':0}
    #Kontrollime ridu
    for rida in maatriks:
        rida_count = 0
        viimane_sümbol = None
        for sümbol in rida:
            if rida_count >= 3:
                tulemus[viimane_sümbol] += 1
            
            if sümbol == viimane_sümbol and sümbol != ' ':
                rida_count += 1
            elif sümbol != ' ':
                rida_count = 1
                viimane_sümbol = sümbol
            else:
                viimane_sümbol = None
                rida_count = 0
                
        if rida_count >= 3:
            tulemus[viimane_sümbol] += 1
                
    #Kontrollime tulpasi
    maatriks_transposed = [*zip(*maatriks)] #Transponeerime, et saaks uuesti ridade loogikat kasutada
    for rida in maatriks_transposed:
        rida_count = 0
        viimane_sümbol = None
        for sümbol in rida:
            if rida_count >= 3:
                tulemus[viimane_sümbol] += 1
            
            if sümbol == viimane_sümbol and sümbol != ' ':
                rida_count += 1
            elif sümbol != ' ':
                rida_count = 1
                viimane_sümbol = sümbol
            else:
                viimane_sümbol = None
                rida_count = 0
                
        if rida_count >= 3:
            tulemus[viimane_sümbol] += 1
            
    #Kontrollime diagonaale vasakult paremale alla (kokku 3)
    kontrolli_diagonaali(tulemus, maatriks, 3, 1, 0)
    kontrolli_diagonaali(tulemus, maatriks, 4, 0, 0)     
    kontrolli_diagonaali(tulemus, maatriks, 3, 0, 1)
    
    #Kontrollime diagonaale paremalt vasakule alla, keerates maatriksi tagurpidi
    kontrolli_diagonaali(tulemus, maatriks[::-1], 3, 1, 0)
    kontrolli_diagonaali(tulemus, maatriks[::-1], 4, 0, 0)     
    kontrolli_diagonaali(tulemus, maatriks[::-1], 3, 0, 1)
    
    return tulemus