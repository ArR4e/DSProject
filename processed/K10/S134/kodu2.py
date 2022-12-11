def võitja(maatriks):
    x = 0
    o = 0
    #horisontaal
    for i in range(2):
        for j in range(2):
            tulemus =maatriks[i][j]+maatriks[i][j+1]+maatriks[i][j+2]
            if tulemus == "XXX":
                x+=1
            elif tulemus == "OOO":
                o+=1
    #vertikaal
    for i in range(2):
        for j in range(2):
            tulemus = maatriks[i][j]+maatriks[i+1][j]+maatriks[i+2][j]
            if tulemus == "XXX":
                x+=1
            elif tulemus == "OOO":
                o+=1
    #peadiagonaal
    for i in range(2):
        for j in range(2):
            tulemus = maatriks[i][j]+maatriks[i+1][j+1]
            if tulemus == "XXX":
                x+=1
            elif tulemus == "OOO":
                o+=1
    #kõrvaldiagonaal
    for i in range(2):
        for j in range(2):
            tulemus = maatriks[i][j+1]+maatriks[i+1][j]
            if tulemus == "XXX":
                x+=1
            elif tulemus == "OOO":
                o+=1
    sõnastik = {"X":x, "O":o}
    return sõnastik