#Trips-traps-trull
def võitja(maatriks):
    sümbolid = {"O": 0, "X": 0}
    sagedused = {}
    #horisontaalselt
    m = 0
    n = 0
    for i in range(0,len(maatriks)):
        if maatriks[i].count("X") > 2:
            m +=1
            if maatriks[i].count("X") == 4:
                m +=1
        elif maatriks[i].count("O") > 2:
            n +=1
            if maatriks[i].count("O") == 4:
                n +=1
    #vertikaalselt
    for i in range(0,len(maatriks)):
        x = 0
        y = 0
        for j in range(0,len(maatriks[i])):
            if maatriks[j][i] == "X":
                x += 1
                if x > 2:
                    if x == 4:
                        m += 1
                    else:
                        m += 1
            elif maatriks[j][i] == "O":
                y += 1
                if y > 2:
                    if y == 4:
                        n += 1
                    else:
                        n += 1
    #diagonaalis
    for i in range(0, 2):
        for j in range(0, len(maatriks[i])):
            if j < 2:
                if maatriks[i][j] == maatriks[i+1][j+1] == maatriks[i+2][j+2]:
                    if maatriks[i][j] == "X":
                        m +=1
                    elif maatriks[i][j] == "O":
                        n +=1
            elif j > 1:
                if maatriks[i][j] == maatriks[i+1][j-1] == maatriks[i+2][j-2]:
                    if maatriks[i][j] == "X":
                        m +=1
                    elif maatriks[i][j] == "O":
                        n +=1
    sümbolid["X"] = m
    sümbolid["O"] = n
    return sümbolid

print(võitja([['O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O']]))