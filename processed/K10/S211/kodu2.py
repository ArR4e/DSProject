proov =[[' ', ' ', ' ', ' '],
        [' ', 'X', ' ', ' '],
        [' ', ' ', 'X', ' '],
        [' ', ' ', ' ', 'X']]

def sümbol(süm, maatriks):
    esineb = 0
    for i in range(4): #reas kontroll
        for j in range(2):
            if maatriks[i][j]==maatriks[i][j+1]==maatriks[i][j+2]==süm:
                esineb += 1
    for i in range(2): #veerus kontroll
        for j in range(4):
            if maatriks[i][j]==maatriks[i+1][j]==maatriks[i+2][j]==süm:
                esineb +=1
    for i in range(2): #peadiagonaal kontroll ühtpidi
        for j in range(2):
            if maatriks[i][j]==maatriks[i+1][j+1]==maatriks[i+2][j+2]==süm:
                esineb += 1
    for i in range(2): #peadiagonaal teistpidi, kõrvaldiagonaal
        for j in range(1, -1, -1):  
            if maatriks[i][j+2]==maatriks[i+1][j+1]==maatriks[i+2][j]==süm:
                esineb += 1 
            
    return(esineb)
        
        

def võitja(maatriks):
    
    seis = {}
    seis['X']=sümbol("X", maatriks)
    seis['O']=sümbol("O", maatriks)
    return seis
    