def võitja(maatriks):
    X=0
    O=0
    for i in range(4):
        for j in range(2):
            if maatriks[i][j]==maatriks[i][j+1]==maatriks[i][j+2]=='X': #horisontaalselt
                X +=1
            if maatriks[i][j]==maatriks[i][j+1]==maatriks[i][j+2]=='O':
                O +=1
    for i in range(2):
        for j in range(2):
            if maatriks[i][j]==maatriks[i+1][j+1]==maatriks[i+2][j+2]=='X':#peadiagonaal
                X+=1
            if maatriks[i][j]==maatriks[i+1][j+1]==maatriks[i+2][j+2]=='O':
                O +=1
            if maatriks[i][j+2]==maatriks[i+1][j+1]==maatriks[i+2][j]=='X':#kõrvaldiagonaal
                X +=1
            if maatriks[i][j+2]==maatriks[i+1][j+1]==maatriks[i+2][j]=='O':
                O +=1
    for i in range(2):
        for j in range(4):          
            if maatriks[i][j]==maatriks[i+1][j]==maatriks[i+2][j]=='X': #vertikaalselt
                X +=1
            if maatriks[i][j]==maatriks[i+1][j]==maatriks[i+2][j]=='O':
                O +=1
    sõnastik={}
    sõnastik['X']=X
    sõnastik['O']=O
    return sõnastik
            