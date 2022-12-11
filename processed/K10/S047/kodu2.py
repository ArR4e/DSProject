def luger(täht, maatriks):
    lugeja = 0
    for i in range(len(maatriks)):
        rida = maatriks[i]
        for j in range(len(rida)):
            if i-2 < 0 and j-2 < 0:
                if maatriks[i][j] == täht and maatriks[i+1][j+1] == täht and maatriks[i+2][j+2] == täht: 
                    lugeja += 1
            
            if j-2 < 0:    
                if maatriks[i][j] == täht and maatriks[i][j+1] == täht and maatriks[i][j+2] == täht:
                    lugeja += 1
           
            if i-2 < 0:    
                if maatriks[i][j] == täht and maatriks[i+1][j] == täht and maatriks[i+2][j] == täht:
                    lugeja += 1
            
            if i-2 < 0 and j-2 >= 0:
                if maatriks[i][j] == täht and maatriks[i+1][j-1] == täht and maatriks[i+2][j-2] == täht:
                    lugeja += 1

    return(täht, lugeja)




def võitja(maatriks):
    
    o=luger("O", maatriks)
    x=luger("X", maatriks)  
    
    sõnastik = {}
    sõnastik[o[0]] = o[1]
    sõnastik[x[0]] = x[1]
    return sõnastik


maatriks = [['O',' ','O',' '],
            ['O','O',' ',' '],
            [' ',' ','O','O'],
            [' ',' ',' ','O']]
                       
print(võitja(maatriks))    
            