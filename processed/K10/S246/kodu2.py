def võitja(maatriks):
    xloendur = 0
    oloendur = 0
    for i in range(len(maatriks)):    
        for j in range(len(maatriks[i])):
            if j <= 1:
                if maatriks [i][j] == 'X' and maatriks[i][j+1] == 'X' and maatriks[i][j+2] == 'X':
                    xloendur += 1
                elif maatriks [i][j] == 'O' and maatriks[i][j+1] == 'O' and maatriks[i][j+2] == 'O':
                    oloendur += 1
            if i <= 1:
                if maatriks [i][j] == 'X' and maatriks[i+1][j] == 'X' and maatriks[i+2][j] == 'X':
                    xloendur += 1
                elif maatriks [i][j] == 'O' and maatriks[i+1][j] == 'O' and maatriks[i+2][j] == 'O':
                    oloendur += 1
            if j <= 1 and i <= 1:
                 if maatriks [i][j] == 'X' and maatriks[i+1][j+1] == 'X' and maatriks[i+2][j+2] == 'X':
                    xloendur += 1
                 elif maatriks [i][j] == 'O' and maatriks[i+1][j+1] == 'O' and maatriks[i+2][j+2] == 'O':
                    oloendur += 1
            if j >= 2 and i <= 1:
                if maatriks [i][j] == 'X' and maatriks[i+1][j-1] == 'X' and maatriks[i+2][j-2] == 'X':
                    xloendur += 1
                elif maatriks [i][j] == 'O' and maatriks[i+1][j-1] == 'O' and maatriks[i+2][j-2] == 'O':
                    oloendur += 1
    vastus = {'O': oloendur, 'X': xloendur}
    return vastus