import numpy as np
def võitja(x):
    seis = {}
    if x == []:
        seis['O'] = 0
        seis['X'] = 0
        return seis
    a = ''
    X = 0
    O = 0
    for i in x:
        a = ''.join(i)
        if a == 'XXXX':
            X += 2
        elif 'XXX' in a:
            X += 1
        elif 'OOOO' in a:
            O += 2
        elif 'OOO' in a:
            O += 1 

    y = np.transpose(x)
    a = ''
    for i in y:
        a = ''.join(i)
        if a == 'XXXX':
            X += 2
        elif 'XXX' in a:
            X += 1
        elif 'OOOO' in a:
            O += 2
        elif 'OOO' in a:
            O += 1
    if len(set([x[i+1][i+1] for i in range(3)])) == 1 or len(set([x[i][i] for i in range(3)])) == 1:
        if len(set([x[i][i] for i in range(len(x))])) == 1:
            if x[0][0] == 'X':
                X += 2
            elif x[0][0] == 'O':
                O += 2
        else:
            if x[1][1] == 'X':
                X += 1
            elif x[1][1] == 'O':
                O += 1
    if len(set([x[i+1][len(x)-i-2] for i in range(3)])) == 1 or len(set([x[i][len(x)-1-i] for i in range(3)])) == 1:
        if len(set([x[i][len(x)-i-1] for i in range(len(x))])) == 1:
            if x[1][-2] == 'X':
                X += 2
            elif x[1][-2] == 'O':
                O += 2
        else:
            if x[1][-2] == 'X':
                X += 1
            elif x[1][-2] == 'O':
                O += 1       
    if x[0][1] == x[1][2] and x[0][1] == x[2][3]:
        if x[0][1] == 'X':
                X += 1
        elif x[0][1] == 'O':
                O += 1
    if x[0][2] == x[1][1] and x[0][2] == x[2][0]:
        if x[0][2] == 'X':
                X += 1
        elif x[0][2] == 'O':
                O += 1
    if x[1][0] == x[2][1] and x[1][0] == x[3][2]:
        if x[1][0] == 'X':
                X += 1
        elif x[1][0] == 'O':
                O += 1
    if x[1][3] == x[2][2] and x[1][3] == x[3][1]:
        if x[1][3] == 'X':
                X += 1
        elif x[1][3] == 'O':
                O += 1
    seis['O'] = O
    seis['X'] = X
    return seis
print(võitja( [[' ', 'O', 'X', ' '],
               ['O', 'X', 'O', 'X'],
               ['X', 'O', 'X', 'O'],
               [' ', 'X', 'O', ' ']]))


