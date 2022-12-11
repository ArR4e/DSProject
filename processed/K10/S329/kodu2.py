# 2. Trips-traps-trull

def võitja(maatriks):
    X_loendur = 0
    O_loendur = 0
    for el in range(0, 4):
        for i in range(0, 2):
            if (maatriks[el][0 + i] == maatriks[el][1 + i] == maatriks[el][2 + i]) == True:
                sümbol = maatriks[el][0 + i]
                if sümbol == 'X':
                    X_loendur += 1
                elif sümbol == 'O':
                    O_loendur += 1
    for i in range(0, 4):
        for el in range(0, 2):
            if (maatriks[0 + el][i] == maatriks[1 + el][i] == maatriks[2 + el][i]) == True:
                sümbol = maatriks[0 + el][i]
                if sümbol == 'X':
                    X_loendur += 1
                elif sümbol == 'O':
                    O_loendur += 1
    for el in range(0, 2):
        for i in range(0, 2):
            if (maatriks[0 + el][0 + i] == maatriks[1 + el][1 + i] == maatriks[2 + el][2 + i]) == True:
                sümbol = maatriks[0 + el][0 + i]
                if sümbol == 'X':
                    X_loendur += 1
                elif sümbol == 'O':
                    O_loendur += 1
    for el in range(0, 2):
        for i in range(0, 2):
            if (maatriks[0 + el][0 - (i + 1)] == maatriks[1 + el][-1 - (i + 1)] == maatriks[2 + el][-2 - (i + 1)]) == True:
                sümbol = maatriks[0 + el][0 - (i + 1)]
                if sümbol == 'X':
                    X_loendur += 1
                elif sümbol == 'O':
                    O_loendur += 1
    return {'O': O_loendur, 'X': X_loendur}
    

#maatriks = [['O','O','O','X'],
#         [' ',' ','X','O'],
#         [' ','X',' ','O'],
#         ['X','X','X','O']]
#vastus = võitja(maatriks)
#print(vastus)
