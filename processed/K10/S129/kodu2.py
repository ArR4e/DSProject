#trips-traps-trull


def võitja(maatriks):
    x = 0
    o = 0
    d = {}
    
    #horisontaal
    for i in maatriks:
        if i.count("X") == 3:
            x += 1
        elif i.count("X") == 4:
            x += 2
                
        elif i.count("O") == 3:
            o += 1
        elif i.count("O") == 4:
            o += 2
        
    #vertikaal
    for i in range(2):
        for j in range(4):
            if maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j] == "X":
                x += 1
                
            if maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j] == "O":
                o += 1

    #üks diagonaal
    for i in range(2):
        for j in range(2):
            if maatriks[i][j] == maatriks[i+1][j+1] == maatriks[i+2][j+2] == "X":
                x += 1
            
            if maatriks[i][j] == maatriks[i+1][j+1] == maatriks[i+2][j+2] == "O":
                o += 1

    #teine diagonaal    
    for i in range(2):
        for j in range(2):
            if maatriks[i][j+2] == maatriks[i+1][j+1] == maatriks[i+2][j] == "X":
                x += 1
            
            if maatriks[i][j+2] == maatriks[i+1][j+1] == maatriks[i+2][j] == "O":
                o += 1
    
    d["O"] = o
    d["X"] = x
    
    return d



x = ([['X',' ',' ','O'],
      [' ','X','O','O'],
      [' ','O','X','O'],
      ['O',' ',' ','X']])

print(võitja(x))