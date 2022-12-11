def võitja(mäng):
    x_count = 0
    o_count = 0
    for i in range(len(mäng)):
        #horizontaal
        if mäng[i].count('X') == 4:
            x_count += 2
        elif mäng[i].count('X') == 3:
            if (mäng[i][0] == 'X' or mäng[i][3] == 'X') and mäng[i][1] == 'X' and mäng[i][2] == 'X':
                x_count += 1
        
        if mäng[i].count('O') == 4:
            o_count += 2
        elif mäng[i].count('O') == 3:
            if (mäng[i][0] == 'O' or mäng[i][3] == 'O') and mäng[i][1] == 'O' and mäng[i][2] == 'O':
                o_count += 1
                
    #vertikaal
    for i in range(4):
        for j in range(2):
            if mäng[j][i] == 'O' and mäng[j+1][i] == 'O' and mäng[j+2][i] == 'O':
                o_count += 1
            elif mäng[j][i] == 'X' and mäng[j+1][i] == 'X' and mäng[j+2][i] == 'X':
                x_count += 1
    
    #diagonaal 1
    for i in range(2):
        for j in range(4):
            if j <= 1:
                if mäng[i][j] == 'O' and mäng[i+1][j+1] == 'O' and mäng[i+2][j+2] == 'O':
                    o_count += 1
                elif mäng[i][j] == 'X' and mäng[i+1][j+1] == 'X' and mäng[i+2][j+2] == 'X':
                    x_count += 1
            else:
                if mäng[i][j] == 'O' and mäng[i+1][j-1] == 'O' and mäng[i+2][j-2] == 'O':
                    o_count += 1
                elif mäng[i][j] == 'X' and mäng[i+1][j-1] == 'X' and mäng[i+2][j-2] == 'X':
                    x_count += 1
            
    return {'O':o_count, 'X':x_count}


