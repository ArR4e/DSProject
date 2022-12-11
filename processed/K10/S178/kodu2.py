def võitja(maatriks):
    o_kogus = 0
    x_kogus = 0
    x_seis = 0
    o_seis = 0
    sõnastik = {}
    for rida in maatriks:
        for element in rida:
            if 'X' in element:
                x_kogus += 1   
            elif 'O' in element:
                o_kogus += 1    
    if x_kogus < 3 and o_kogus < 3:
        return({'O': o_seis, 'X': x_seis})
#horisontaalselt
    elif x_kogus >= 3 or o_kogus >= 3:
        for i in range(4):
            for j in range(2):
                if maatriks[i][j]+maatriks[i][j+1]+maatriks[i][j+2] == 'XXX':
                    x_seis += 1
                elif maatriks[i][j]+maatriks[i][j+1]+maatriks[i][j+2] == 'OOO':
                    o_seis += 1
#vertikaalselt 
        for i in range(2):
            for j in range(4):
                if maatriks[i][j]+maatriks[i+1][j]+maatriks[i+2][j] == 'XXX':
                    x_seis += 1
                elif maatriks[i][j]+maatriks[i+1][j]+maatriks[i+2][j] == 'OOO':
                    o_seis += 1
#peadiagonaal                    
        for i in range(2):
            for j in range(2):
                if maatriks[i][j]+maatriks[i+1][j+1]+maatriks[i+2][j+2] == 'XXX':
                    x_seis += 1
                elif maatriks[i][j]+maatriks[i+1][j+1]+maatriks[i+2][j+2] == 'OOO':
                    o_seis += 1
#teinediagonaaal        
        for i in range(2):
            for j in range(2):
                if maatriks[i][j+2]+maatriks[i+1][j+1]+maatriks[i+2][j] == 'XXX':
                    x_seis += 1
                elif maatriks[i][j+2]+maatriks[i+1][j+1]+maatriks[i+2][j] == 'OOO':
                    o_seis += 1
       
        sõnastik = {'O' : o_seis,'X' : x_seis}
        return(sõnastik)


