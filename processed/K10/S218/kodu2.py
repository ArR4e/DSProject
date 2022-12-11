def võitja(maatriks):
    tulemus = {"X":0, "O":0}
    x= 0
    o = 0
    sümbolid = ["X", "O"]
    
    #read ja veerud
    if maatriks[0][0] == maatriks [0][1] == maatriks[0][2] in sümbolid:
        if maatriks[0][0]== "X":
            x = x+1
        elif maatriks[0][0] == "O":
            o = o+1
    
    if maatriks[0][1] == maatriks [0][2] == maatriks[0][3] in sümbolid:
        if maatriks[0][1]== "X":
            x = x+1
        elif maatriks[0][1] == "O":
            o = o+1
    
    if maatriks[1][0] == maatriks [1][1] == maatriks[1][2] in sümbolid:
        if maatriks[1][0]== "X":
            x = x+1
        elif maatriks[1][0] == "O":
            o = o+1
    if maatriks[1][1] == maatriks [1][2] == maatriks[1][3] in sümbolid:
        if maatriks[1][1]== "X":
            x = x+1
        elif maatriks[1][1] == "O":
            o = o+1
    
    if maatriks[2][0] == maatriks [2][1] == maatriks[2][2] in sümbolid:
        if maatriks[2][0]== "X":
            x = x+1
        elif maatriks[2][0] == "O":
            o = o+1
    if maatriks[2][1] == maatriks [2][2] == maatriks[2][3] in sümbolid:
        if maatriks[2][1]== "X":
            x = x+1
        elif maatriks[2][1] == "O":
            o = o+1
    if maatriks[3][0] == maatriks [3][1] == maatriks[3][2] in sümbolid:
        if maatriks[3][0]== "X":
            x = x+1
        elif maatriks[3][0] == "O":
            o = o+1
    if maatriks[3][1] == maatriks [3][2] == maatriks[3][3] in sümbolid:
         if maatriks[3][1]== "X":
            x = x+1
         elif maatriks[3][1] == "O":
            o = o+1
    
    if maatriks[0][0] == maatriks [1][0] == maatriks[2][0] in sümbolid:
        if maatriks[0][0]== "X":
            x = x+1
        elif maatriks[0][0] == "O":
            o = o+1
    if maatriks[1][0] == maatriks [2][0] == maatriks[3][0] in sümbolid:
        if maatriks[1][0]== "X":
            x = x+1
        elif maatriks[1][0] == "O":
            o = o+1
        
    if maatriks[0][1] == maatriks [1][1] == maatriks[2][1] in sümbolid:
        if maatriks[0][1]== "X":
            x = x+1
        elif maatriks[0][1] == "O":
            o = o+1
    if maatriks[1][1] == maatriks [2][1] == maatriks[3][1] in sümbolid:
        if maatriks[1][1]== "X":
            x = x+1
        elif maatriks[1][1] == "O":
            o = o+1
    
    if maatriks[0][2] == maatriks [1][2] == maatriks[2][2] in sümbolid:
        if maatriks[0][2]== "X":
            x = x+1
        elif maatriks[0][2] == "O":
            o = o+1
    if maatriks[1][2] == maatriks [2][2] == maatriks[3][2] in sümbolid:
        if maatriks[1][2]== "X":
            x = x+1
        elif maatriks[1][2] == "O":
            o = o+1
        
    if maatriks[0][3] == maatriks [1][3] == maatriks[2][3] in sümbolid:
        if maatriks[0][3]== "X":
            x = x+1
        elif maatriks[0][3] == "O":
            o = o+1
    if maatriks[1][3] == maatriks [2][3] == maatriks[3][3] in sümbolid:
        if maatriks[1][3]== "X":
            x = x+1
        elif maatriks[1][3] == "O":
            o = o+1
#diagonaalid
    if maatriks[0][0] == maatriks [1][1] == maatriks[2][2] in sümbolid:
         if maatriks[0][0]== "X":
            x = x+1
         elif maatriks[0][0] == "O":
            o = o+1
    if maatriks[1][1] == maatriks [2][2] == maatriks[3][3] in sümbolid:
         if maatriks[1][1]== "X":
            x = x+1
         elif maatriks[1][1] == "O":
            o = o+1
    if maatriks[0][3] == maatriks [1][2] == maatriks[2][1] in sümbolid:
         if maatriks[0][3]== "X":
            x = x+1
         elif maatriks[0][3] == "O":
            o = o+1
    if maatriks[1][2] == maatriks [2][1] == maatriks[3][0] in sümbolid:
         if maatriks[1][2]== "X":
            x = x+1
         elif maatriks[1][2] == "O":
            o = o+1
    if maatriks[2][0] == maatriks [1][1] == maatriks[0][2] in sümbolid:
        if maatriks[2][0]== "X":
            x = x+1
        elif maatriks[2][0] == "O":
            o = o+1
    if maatriks[3][1] == maatriks [2][2] == maatriks[1][3] in sümbolid:
        if maatriks[3][1]== "X":
            x = x+1
        elif maatriks[3][1] == "O":
            o = o+1
    if maatriks[0][1] == maatriks [1][2] == maatriks[2][3] in sümbolid:
        if maatriks[0][1]== "X":
            x = x+1
        elif maatriks[0][1] == "O":
            o = o+1
    if maatriks[1][0] == maatriks [2][1] == maatriks[3][2] in sümbolid:
        if maatriks[1][0]== "X":
            x = x+1
        elif maatriks[1][0] == "O":
            o = o+1
    
    tulemus["X"]= x
    tulemus["O"]= o
    return tulemus
   
print(võitja([['O',' ',' ','X'],
            [' ','O','X',' '],
            [' ','X','O',' '],
            ['X',' ',' ','O']]))
    