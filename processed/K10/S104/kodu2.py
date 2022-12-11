def võidud(m, sümbol):
    kokku = 0
    #ridades
    for i in range(len(m)):
        for j in range (len(m[i]) - 3):
            if m[i][j] == m[i][j + 1] == m[i][j + 2] == m[i][j + 3] == sümbol:
                kokku += 1
    #veergudes
    for i in range(len(m) - 3):
        for j in range (len(m[i])):
            if m[i][j] == m[i + 1][j] == m[i + 2][j] == m[i + 3][j] == sümbol:
                kokku += 1
    #diagonaalides
    for i in range(len(m) - 3):
        for j in range (len(m[i]) - 3):
            if m[i][j] == m[i + 1][j + 1] == m[i + 2][j + 2] == m[i + 3][j + 3] == sümbol:
                kokku += 1
    #teine diagonaal
    for i in range(len(m) - 3):
        for j in range (3, len(m[i])):
            if m[i][j] == m[i + 1][j - 1] == m[i + 2][j - 2] == m[i + 3][j - 3] == sümbol:
                kokku += 1
    return kokku

def võitja(m):
    võite_O = võidud(m, 'O')
    võite_X = võidud(m, 'X')
    return ('O' võite_O, 'X' võite_X)