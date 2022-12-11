def võitja(järjend):
    Ovõite=0
    Xvõite=0
    
    for i in range(2):
        for j in range(4):
            if järjend[i][j] == 'O' and järjend[i+1][j] == 'O' and järjend[i+2][j] == 'O':
                Ovõite +=1
            if järjend[i][j] == 'X' and järjend[i+1][j] == 'X' and järjend[i+2][j] == 'X':
                Xvõite +=1
            if järjend[j][i] == 'O' and järjend[j][i+1] == 'O' and järjend[j][i+2] == 'O':
                Ovõite +=1
            if järjend[j][i] == 'X' and järjend[j][i+1] == 'X' and järjend[j][i+2] == 'X':
                Xvõite +=1
    for i in range(2):
        for j in range(2):
            
            if järjend[i][j] == 'O' and järjend[i+1][j+1] == 'O' and järjend[i+2][j+2] == 'O':
                Ovõite += 1
            if järjend[i][j] == 'X' and järjend[i+1][j+1] == 'X' and järjend[i+2][j+2] == 'X':
                Xvõite += 1
            if järjend[i-2][j] == 'O' and järjend[i-3][j+1] == 'O' and järjend[i-4][j+2] == 'O':
                Ovõite +=1
            if järjend[i-2][j] == 'X' and järjend[i-3][j+1] == 'X' and järjend[i-4][j+2] == 'X':
                Xvõite +=1
    
    return {'O': Ovõite, 'X': Xvõite}
