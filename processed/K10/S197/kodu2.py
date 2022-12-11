def võitja(m):
    O = 0
    X = 0
    seis = {'O': 0, 'X': 0}
    for i in range(4):
        for j in range(2):
            #Horisontaalid
            if m[i][j] == m[i][j+1] and m[i][j] == m[i][j+2]:
                if m[i][j] == 'O' or m[i][j] == 'X': seis[m[i][j]] = seis[m[i][j]] + 1
            #Vertikaalid
            if m[j][i] == m[j+1][i] and m[j][i] == m[j+2][i]:
                if m[j][i] == 'O' or m[j][i] == 'X': seis[m[j][i]] = seis[m[j][i]] + 1
    #Diagonaalid
    for i in range(2):
        if m[i][i] == m[i+1][i+1] and m[i][i] == m[i+2][i+2]:
            if m[i][i] == 'O' or m[i][i] == 'X': seis[m[i][i]] = seis[m[i][i]] + 1
        if m[i][-i-1] == m[i+1][-i-2] and m[i][-i-1] == m[i+2][-i-3]:
            if m[i][-i-1] == 'O' or m[i][-i-1] == 'X': seis[m[i][-i-1]] = seis[m[i][-i-1]] + 1
        if m[i][-i+1] == m[i+1][-i+2] and m[i][-i+1] == m[i+2][-i+3]:
            if m[i][-i+1] == 'O' or m[i][-i+1] == 'X': seis[m[i][-i+1]] = seis[m[i][-i+1]] + 1
        if m[i][i+2] == m[i+1][i+1] and m[i][i+2] == m[i+2][i]:
            if m[i][i+2] == 'O' or m[i][i+2] == 'X': seis[m[i][i+2]] = seis[m[i][i+2]] + 1
    return seis