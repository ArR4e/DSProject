def võitja (mx):
    X = 0
    O = 0
    for rida in mx:
        #horisontaalne
        if rida.count('X') == 3:
            X += 1
        elif rida.count('X') == 4:
            X += 2
        if rida.count('O') == 3:
            O += 1
        elif rida.count('O') == 4:
            O += 2
    for i in range(2):
        #veritkaalne
        if mx[i][3] == mx[i+1][3] == mx[i+2][3] == 'X':
            X +=1
        elif mx[i][3] == mx[i+1][3] == mx[i+2][3] == 'O':
            O +=1
        if mx[i][2] == mx[i+1][2] == mx[i+2][2] == 'X':
            X +=1
        elif mx[i][2] == mx[i+1][2] == mx[i+2][2] == 'O':
            O +=1
        for j in range(2):
            #veritkaalne
            if mx[i][j] == mx[i+1][j] == mx[i+2][j] == 'X':
                X +=1
            elif mx[i][j] == mx[i+1][j] == mx[i+2][j] == 'O':
                O +=1
            #diagonaalne
            if mx[i][j] == mx[i+1][j+1] == mx[i+2][j+2] == 'X': 
                X +=1
            elif mx[i][j] == mx[i+1][j+1] == mx[i+2][j+2] == 'O':
                O +=1
            if mx[i][j+2] == mx[i+1][j+1] == mx[i+2][j] == 'X':
                X +=1
            elif mx[i][j+2] == mx[i+1][j+1] == mx[i+2][j] == 'O':
                O +=1
                           
    return {'O':O, 'X':X}    
                