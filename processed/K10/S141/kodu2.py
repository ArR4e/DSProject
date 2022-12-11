def võitja(maatriks):
    skoor = {}
    skoor["O"] = 0
    skoor["X"] = 0
    
    #horisontaalselt
    for i in range(4):
        if maatriks[i] == ["X", "X", "X", " "] or maatriks[i] == [" ", "X", "X", "X"] or maatriks[i] == ["X", "X", "X", "O"] or maatriks[i] == ["O", "X", "X", "X"]:
            skoor["X"] += 1
        if maatriks[i] == ["X", "X", "X", "X"]:
            skoor["X"] += 2
        if maatriks[i] == ["O", "O", "O", " "] or maatriks[i] == [" ", "O", "O", "O"] or maatriks[i] == ["O", "O", "O", "X"] or maatriks[i] == ["X", "O", "O", "O"]:
            skoor["O"] += 1
        if maatriks[i] == ["O", "O", "O", "O"]:
            skoor["O"] += 2

    #vertikaalselt    
    for j in range(4):
        for i in range(2):
            if maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j] == "X" :
                skoor["X"] += 1     
            if maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j] == "O":
                skoor["O"] += 1
    #risti-rästi
    for i in range(2):
        for j in range(2):
            if maatriks[i][j] == maatriks[i+1][j+1] == maatriks[i+2][j+2] == "X":
                skoor["X"] += 1
            if maatriks[i][j] == maatriks[i+1][j+1] == maatriks[i+2][j+2] == "O":
                skoor["O"] += 1
                
    for i in range(2):
        for j in range(2):
            if maatriks[i][j+2] == maatriks[i+1][j+1] == maatriks[i+2][j] == "X":
                skoor["X"] += 1
            if maatriks[i][j+2] == maatriks[i+1][j+1] == maatriks[i+2][j] == "O":
                skoor["O"] += 1
                
    return skoor
