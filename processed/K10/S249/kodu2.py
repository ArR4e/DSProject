def võitja(maatriks):
    x_punkt = 0
    o_punkt = 0
    
    
    #horisontaal
    for järjend in maatriks:
        for i in range(4):
            for j in range(2):
                if maatriks[i][j]+maatriks[i][j+1]+maatriks[i][j+2] == "XXX":
                    x_punkt += 1
                        
                elif maatriks[i][j]+maatriks[i][j+1]+maatriks[i][j+2] == "OOO":
                    o_punkt += 1
        break
    
    #Vertikaal
    for järjend in maatriks:
        for i in range(2):
            for j in range(4):
                if maatriks[i][j]+maatriks[i+1][j]+maatriks[i+2][j] == "XXX":
                    x_punkt += 1

                elif maatriks[i][j]+maatriks[i+1][j]+maatriks[i+2][j] == "OOO":
                    o_punkt += 1
        break
    
    #diagonaal
    for järjend in maatriks:
        for i in range (2):
            for j in range(2):
                if maatriks[i][j]+maatriks[i+1][j+1]+maatriks[i+2][j+2] == "XXX":
                    x_punkt += 1

                elif maatriks[i][j]+maatriks[i+1][j+1]+maatriks[i+2][j+2] == "OOO":
                    o_punkt += 1
        break
    
    #diagonaal2
    for järjend in maatriks:
        for i in range (2):
            for j in range(2):
                if maatriks[i][j+2]+maatriks[i+1][j+1]+maatriks[i+2][j+0] == "XXX":
                    x_punkt += 1

                elif maatriks[i][j+2]+maatriks[i+1][j+1]+maatriks[i+2][j+0] == "OOO":
                    o_punkt += 1
        break
    
    sõnastik = {}
    sõnastik["O"] = o_punkt
    sõnastik["X"] = x_punkt
    
    return sõnastik