def võitja(maatriks):
    orida=0
    otulp=0
    odiag=0
    xrida=0
    xtulp=0
    xdiag=0

    for i in range(len(maatriks)):
        for j in range(len(maatriks[i])):
            if i<len(maatriks)-2:
                if maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j] in "XO":
                    if maatriks[i][j]=="O":
                        otulp+=1
                    else:
                        xtulp+=1
            if j<len(maatriks[i])-2:
                if maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2] in "XO":
                    if maatriks[i][j]=="O":
                        orida+=1
                    else:
                        xrida+=1
            if i<len(maatriks)-2: # Diagonaalid
                if j<len(maatriks[i])-2:
                    if maatriks[i][j]==maatriks[i+1][j+1]==maatriks[i+2][j+2] in "XO": # diagonaal paremale
                        if maatriks[i][j]=="O":
                            odiag+=1
                        else:
                            xdiag+=1
                    
                if j>1:
                    if maatriks[i][j]==maatriks[i+1][j-1]==maatriks[i+2][j-2] in "XO": # diagonaal vasakule
                        if maatriks[i][j]=="O":
                            odiag+=1
                        else:
                            xdiag+=1
                    
    o=(otulp+orida+odiag)
    x=(xtulp+xrida+xdiag)
    
    return {"O":o,"X":x}