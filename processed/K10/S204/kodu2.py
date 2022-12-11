maatriks=["X", "X", "O", "X"], ["O", "O", "X", "X"], ["X", "X", "O", "X"], ["O", "O", "O", "O"]
def võitja(maatriks):
    X_loendur = 0
    O_loendur = 0
    m=0
    n=0
    for el in range(len(maatriks)):
        #if maatriks[m][n] == "X":
            #X_loendur += 1
            
        #if maatriks[m][n] == "O":
            #O_loendur += 1
            
        for el_2 in range (len(maatriks[0])):
            if maatriks[m][n] == "X":
                X_loendur += 1
            
            if maatriks[m][n] == "O":
                O_loendur += 1
            n+=1
    m+=1
    return X_loendur, O_loendur


print(võitja(maatriks))