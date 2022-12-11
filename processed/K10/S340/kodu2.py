def võitja(maatriks):
    X_loendur=0
    Y_loendur=0
    sõnastik={}
    for i in range(4):
        for j in range(2):
            sümbol=maatriks[i][j]
            if sümbol=="X":
                if maatriks[i][j]==maatriks[i][j+1]==maatriks[i][j+2]=="X":
                    X_loendur+=1
            if sümbol=="O":
                if maatriks[i][j]==maatriks[i][j+1]==maatriks[i][j+2]=="O":
                    Y_loendur+=1
    for i in range(2):
        for j in range(4):
            sümbol=maatriks[i][j]
            if sümbol=="X":
                if maatriks[i][j]==maatriks[i+1][j]==maatriks[i+2][j]=="X":
                    X_loendur+=1
            if sümbol=="O":
                if maatriks[i][j]==maatriks[i+1][j]==maatriks[i+2][j]=="O":
                    Y_loendur+=1
        for j in range(2):
            sümbol=maatriks[i][j]
            if sümbol=="X":
                if maatriks[i][j]==maatriks[i+1][j+1]==maatriks[i+2][j+2]=="X":
                    X_loendur+=1
            if sümbol=="O":
                if maatriks[i][j]==maatriks[i+1][j+1]==maatriks[i+2][j+2]=="O":
                    Y_loendur+=1
        for j in range(2,4):
            sümbol=maatriks[i][j]
            if sümbol=="X":
                if maatriks[i][j]==maatriks[i+1][j-1]==maatriks[i+2][j-2]=="X":
                    X_loendur+=1
            if sümbol=="O":
                if maatriks[i][j]==maatriks[i+1][j-1]==maatriks[i+2][j-2]=="O":
                    Y_loendur+=1
    sõnastik["O"]=Y_loendur
    sõnastik["X"]=X_loendur
    return sõnastik