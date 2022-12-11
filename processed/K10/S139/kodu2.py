def võitja(mtrx):
    O_count = 0
    X_count = 0
    #rea kaupa kontroll
    for x in mtrx:
        if x[0] ==  x[1] ==  x[2]:
            if x[0] == "X":
                X_count += 1
            if x[0] == "O":
                O_count += 1
        if x[3] == x[2] == x[1]:
            if x[3] == "X":
                X_count += 1
            if x[3] == "O":
                O_count += 1
    #veeru kaupa kontroll
    for i in range(len(mtrx)):
        if mtrx[0][i] == mtrx[1][i] == mtrx[2][i]:
            if mtrx[0][i] == "X":
                X_count += 1
            if mtrx[0][i] == "O":
                O_count += 1
        if mtrx[3][i] == mtrx[2][i] == mtrx[1][i]:
            if mtrx[3][i] == "X":
                X_count += 1
            if mtrx[3][i] == "O":
                O_count += 1
    #diagonaalide kaupa vasakult paremale
    if mtrx[0][0] == mtrx[1][1] == mtrx[2][2]:
        if mtrx[0][0] == "X":
            X_count += 1
        if mtrx[0][0] == "O":
            O_count += 1
    if mtrx[1][0] == mtrx[2][1] == mtrx[3][2]:
        if mtrx[1][0] == "X":
            X_count += 1
        if mtrx[1][0] == "O":
            O_count += 1
    if mtrx[0][1] == mtrx[1][2] == mtrx[2][3]:
        if mtrx[0][1] == "X":
            X_count += 1
        if mtrx[0][1] == "O":
            O_count += 1
    if mtrx[1][1] == mtrx[2][2] == mtrx[3][3]:
        if mtrx[1][1] == "X":
            X_count += 1
        if mtrx[1][1] == "O":
            O_count += 1
    #paremalt vasakule
    if mtrx[1][3] == mtrx[2][2] == mtrx[3][1]:
        if mtrx[1][3] == "X":
            X_count += 1
        if mtrx[1][3] == "O":
            O_count += 1
    if mtrx[0][3] == mtrx[1][2] == mtrx[2][1]:
        if mtrx[0][3] == "X":
            X_count += 1
        if mtrx[0][3] == "O":
            O_count += 1
    if mtrx[1][2] == mtrx[2][1] == mtrx[3][0]:
        if mtrx[1][2] == "X":
            X_count += 1
        if mtrx[1][2] == "O":
            O_count += 1
    if mtrx[0][2] == mtrx[1][1] == mtrx[2][0]:
        if mtrx[0][2] == "X":
            X_count += 1
        if mtrx[0][2] == "O":
            O_count += 1
        
    win = {"O":O_count, "X":X_count}
    return win



print(võitja([['X','X','X',' '],
              [' ','O',' ',' '],
              [' ',' ','O',' '],
              [' ',' ',' ','O']]))
                