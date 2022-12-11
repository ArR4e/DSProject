def võitja(mäng):
    
    x = 0
    o = 0
    O = {}
    X = {}
    
    for i in range(2):
        for j in range(2):
               if mäng[i][j] == mäng[i + 1][j + 1] == mäng[i + 2][j + 2] == 'X':
                   x += 1
                
    for i in range(4):
        for j in range(2):
            if mäng[i][j] == mäng[i][j + 1] == mäng[i][j + 2] == 'X':
                x += 1
            
    for i in range(2):
        for j in range(4):
           if mäng[i][j] == mäng[i + 1][j] == mäng[i + 2][j] == 'X':
               x += 1
            
    for i in range(2):
        for j in range(2):
            if mäng[i + 2][j] == mäng[i + 1][j + 1] == mäng[i][j + 2] == 'X':
                x += 1
                
    for i in range(2):
        for j in range(2):
                if mäng[i][j] == mäng[i + 1][j + 1] == mäng[i + 2][j + 2] == 'O':
                    o += 1
                
    for i in range(4):
        for j in range(2):
            if mäng[i][j] == mäng[i][j + 1] == mäng[i][j + 2] == 'O':
                o += 1
            
    for i in range(2):
        for j in range(4):
            if mäng[i][j] == mäng[i + 1][j] == mäng[i + 2][j] == 'O':
                o += 1
            
    for i in range(2):
        for j in range(2):
            if mäng[i + 2][j] == mäng[i + 1][j + 1] == mäng[i][j + 2] == 'O':
                o += 1
                
    X['X'] = x
    O['O']= o
    koos = {**X, **O}
    return koos
