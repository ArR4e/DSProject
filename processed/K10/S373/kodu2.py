def võitja(maatriks):
    sõnastik = {}
    summa = 0
    arv_O = 0
    arv_X= 0
    
    for i in range(4):
        for j in range(2):
            summa = maatriks[i][j] + maatriks[i][j+1] + maatriks[i][j+2]
            if summa == "XXX":
                arv_X += 1
            if summa == "OOO":
                arv_O += 1
                
    for i in range(2):
        for j in range(4):
            summa = maatriks[i][j] + maatriks[i+1][j] + maatriks[i+2][j]
            if summa == "XXX":
                arv_X += 1
            if summa == "OOO":
                arv_O += 1
                
    for i in range(2):
        for j in range(2):
            summa = maatriks[i][j] + maatriks[i+1][j+1] + maatriks[i+2][j+2]
            if summa == "XXX":
                arv_X += 1
            if summa == "OOO":
                arv_O += 1
                
    for i in range(2):
        for j in range(2):
            summa = maatriks[i][j+2] + maatriks[i+1][j+1] + maatriks[i+2][j]
            if summa == "XXX":
                arv_X += 1
            if summa == "OOO":
                arv_O += 1
                
    sõnastik = {"O": arv_O, "X": arv_X}
    return sõnastik