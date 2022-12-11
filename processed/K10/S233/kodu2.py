def võitja(maatriks):
    x=0
    o=0
    for i in range(4):
        for j in range(2):
            #Horisontaalne lugemine
            if maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2]=="X":
                x+=1
            if maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2]=="O":
                o+=1
    for i in range(2):
        for j in range(2):
            #Diagonaalide lugemine
            if maatriks[i][j] == maatriks[i+1][j+1]== maatriks[i+2][j+2]=="X":
                x+=1
            if maatriks[i][j] == maatriks[i+1][j+1]== maatriks[i+2][j+2]=="O":
                o+=1
            if maatriks[i][j+2] == maatriks[i+1][j+1]== maatriks[i+2][j] == "X":
                x+=1
            if maatriks[i][j+2] == maatriks[i+1][j+1]== maatriks[i+2][j] == "O":
                o+=1
    for i in range(2):
        for j in range(4):
            #Vertikaalne lugemine
            if maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j]=="X":
                x+=1
            if maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j]=="O":
                o+=1
    return {"O": o, "X": x}