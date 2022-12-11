def võitja(matrix):
    foo = {}
    x = 0
    o = 0
    n = 0
    m = 0
    for i in matrix:
        if i.count('X') > 2:
            x += i.count('X') - 2
        elif i.count('O') > 2:
            o += i.count('O') - 2
            
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[j][i] == 'X':
                n += 1
            elif matrix[j][i] == 'O':
                m += 1
        if n > 2:
            x = n - 2
            
        elif m > 2:
            o = m - 2
    n = 0
    m = 0
    for i in range(len(matrix)):
        if matrix[i][i] == 'X':
            n += 1
        elif matrix[i][i] == 'O':
            m += 1
    if n > 2:
        x = n - 2
    if m > 2:
        o = m - 2
    n = 0
    m = 0
    #ei mõelnud välja, kuidas ilma 5 lisa for loopita programmi teha
    
    foo['O'] = o
    foo['X'] = x
    return foo