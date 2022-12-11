def võitja(jär):
    d = {}
    xid = 0
    od = 0
    for i in range(4):
        for j in range(2):
            if jär[i][j] == jär[i][j+1] == jär[i][j+2]:
                if jär[i][j] == 'X':
                    xid += 1
                if jär[i][j] == 'O':
                    od += 1
    for i in range(2):
        for j in range(4):
            if jär[i][j] == jär[i+1][j] == jär[i+2][j]:
                if jär[i][j] == 'X':
                    xid += 1
                if jär[i][j] == 'O':
                    od += 1
    for i in range(2):
        for j in range(2):
            if jär[i][j] == jär[i+1][j+1] == jär[i+2][j+2]:
                if jär[i][j] == 'X':
                    xid += 1
                if jär[i][j] == 'O':
                    od += 1
    for i in range(2):
        for j in range(2):
            if jär[i][j+2] == jär[i+1][j+1] == jär[i+2][j]:
                if jär[i][j+2] == 'X':
                    xid += 1
                if jär[i][j+2] == 'O':
                    od += 1              
    d['O'] = od
    d['X'] = xid
    return d