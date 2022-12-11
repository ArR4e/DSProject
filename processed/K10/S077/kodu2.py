def võitja(maatriks):
    sõnastik={}
    Xvõidud=0
    Ovõidud=0
    for i in range(4): #horisontaalsete jaoks https://progtugi.cs.ut.ee/#/ts/5f958a199e26238c0aa0f400/5f958b659e26238c0aa0f45f
        for j in range(2):
            sõne=""
            sõne+=maatriks[i][j]+maatriks[i][j+1]+maatriks[i][j+2]
            if "XXX" in sõne:
                Xvõidud+=1
            if "OOO" in sõne:
                Ovõidud+=1
    for i in range(2):
        for j in range(4):
            sõne=""
            sõne+=maatriks[i][j]+maatriks[i+1][j]+maatriks[i+2][j]
            if "XXX" in sõne:
                Xvõidud+=1
            if "OOO" in sõne:
                Ovõidud+=1
    for i in range(2):
        for j in range(2):
            sõne=""
            sõne+=maatriks[i][j]+maatriks[i+1][j+1]+maatriks[i+2][j+2]
            if "XXX" in sõne:
                Xvõidud+=1
            if "OOO" in sõne:
                Ovõidud+=1
    for i in range(2):
        for j in range(2):
            sõne=""
            sõne+=maatriks[i][-j-1]+maatriks[i+1][-j-2]+maatriks[i+2][-j-3]
            if "XXX" in sõne:
                Xvõidud+=1
            if "OOO" in sõne:
                Ovõidud+=1
    sõnastik["X"]=Xvõidud
    sõnastik["O"]=Ovõidud
    return sõnastik