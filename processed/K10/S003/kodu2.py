def võitja(maatriks):
    järjend = []
    sõnastik = {"O":0, "X":0}
    for i in range(4):
        for j in range(2):
            järjend.append(maatriks[i][j]+maatriks[i][j+1]+maatriks[i][j+2])
    for i in range(2):
        for j in range(4):
            järjend.append(maatriks[i][j]+maatriks[i+1][j]+maatriks[i+2][j])
    for i in range(1):
        for j in range(1):
            järjend.append(maatriks[i][j]+maatriks[i+1][j+1]+maatriks[i+2][j+2])
    for i in range(1):
        for j in range(1):
            järjend.append(maatriks[i+1][j+1]+maatriks[i+2][j+2]+maatriks[i+3][j+3])
    for i in range(1):
        for j in range(3,2,-1):
            järjend.append(maatriks[i][j]+maatriks[i+1][j-1]+maatriks[i+2][j-2])
    for i in range(1):
        for j in range(3,2,-1):
            järjend.append(maatriks[i+1][j-1]+maatriks[i+2][j-2]+maatriks[i+3][j-3])
    
    for i in range(1):
        for j in range(1,2):
            järjend.append(maatriks[i][j]+maatriks[i+1][j+1]+maatriks[i+2][j+2])
    for i in range(1,2):
        for j in range(1):
            järjend.append(maatriks[i][j]+maatriks[i+1][j+1]+maatriks[i+2][j+2])
    
    for i in range(1):
        for j in range(2,1,-1):
            järjend.append(maatriks[i][j]+maatriks[i+1][j-1]+maatriks[i+2][j-2])
            
    for i in range(1,2):
        for j in range(3,2,-1):
            järjend.append(maatriks[i][j]+maatriks[i+1][j-1]+maatriks[i+2][j-2])
    
    
    
            
    for el in järjend:
        if el == "XXX":
            sõnastik["X"] += 1
        if el == "OOO" :
            sõnastik["O"] += 1
            
    return sõnastik


