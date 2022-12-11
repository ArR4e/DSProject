def võitja(maatriks):
    X_loendur = 0
    O_loendur = 0
    sõnastik = {}
    for i in range(4):
        for j in range(2):
            if(maatriks[i][j]==maatriks[i][j+1] and maatriks[i][j+1]==maatriks[i][j+2]): 
                if(maatriks[i][j]=="X"): 
                    X_loendur += 1
                elif (maatriks[i][j]=="O"):
                    O_loendur += 1
    for i in range(2):
        for j in range(4):
            if(maatriks[i][j]==maatriks[i+1][j] and maatriks[i+1][j]==maatriks[i+2][j]):
                if (maatriks[i][j]=="X"):
                     X_loendur += 1
                elif (maatriks[i][j]=="O") :
                    O_loendur += 1
    for i in range(2):
        for j in range(2):
            if (maatriks[i][j]==maatriks[i+1][j+1] and maatriks[i+1][j+1] == maatriks[i+2][j+2]):
                if  (maatriks[i+1][j+1]=="X"):
                     X_loendur += 1
                elif (maatriks[i+1][j+1]=="O"):
                    O_loendur += 1
        
    for i in range(2):
        for j in range(2):
            if (maatriks[3-i][j]==maatriks[2-i][j+1] and maatriks[2-i][j+1]==maatriks[1-i][j+2]):
                if  (maatriks[3-i][j]=="X"):
                     X_loendur += 1
                elif (maatriks[3-i][j]=="O"):
                    O_loendur += 1
                    
    sõnastik["X"] = X_loendur
    sõnastik["O"] = O_loendur
    return sõnastik

