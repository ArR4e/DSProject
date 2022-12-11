def võitja(maatriks):
    sõnastik={}
    X_kokku = 0
    O_kokku = 0
    
    
    for i in range(4):
        for j in range(2):
            if maatriks[i][j] == maatriks [i][j+1] == maatriks[i][j+2] == "X":
               X_kokku+=1
            if maatriks[i][j] == maatriks [i][j+1] == maatriks[i][j+2] == "O":
                O_kokku+=1
    
    for i in range(2):
        for j in range(4):
            if maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j] == "X":
              X_kokku+=1
            if maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j] == "O":
                O_kokku+=1
    
    for i in range (2):
        for j in range(2):
            if maatriks[i][j] == maatriks[i+1][j+1] == maatriks[i+2][j+2] == "X":
              X_kokku+=1
            if maatriks[i][j] == maatriks[i+1][j+1] == maatriks[i+2][j+2] == "O":
                O_kokku+=1
                
    
    for i in range (2):
        for j in range(2):
            if maatriks[3-i][j] == maatriks[3-(i+1)][j+1] == maatriks[3-(i+2)][j+2] == "X":
                X_kokku+=1
            if maatriks[3-i][j] == maatriks[3-(i+1)][j+1] == maatriks[3-(i+2)][j+2] == "O":
                O_kokku+=1
                
    sõnastik["O"]=O_kokku
    sõnastik["X"]=X_kokku
    return sõnastik
        
                                                            
