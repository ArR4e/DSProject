def võitja(x):
    xl = 0
    ol = 0
    s = {}
    for i in range(4):
        for j in range(2):
            if x[i][j] == x[i][j+1] == x[i][j+2] == "X":
                xl += 1
            if x[i][j] == x[i][j+1] == x[i][j+2] == "O":
                ol += 1
    for i in range(2):
        for j in range(4):
            if x[i][j] == x[i+1][j] == x[i+2][j] == "X":
                xl += 1
            if x[i][j] == x[i+1][j] == x[i+2][j] == "O":
                ol += 1
    for i in range(2):
        for j in range(2):
            if x[i][j] == x[i+1][j+1] == x[i+2][j+2] == "X":
                xl += 1
            if x[i][j] == x[i+1][j+1] == x[i+2][j+2] == "O":
                ol += 1
    for i in range(2):
        for j in range(2):
            if x[i+2][j] == x[i+1][j+1] == x[i][j+2] == "X":
                xl += 1
            if x[i+2][j] == x[i+1][j+1] == x[i][j+2] == "O":
                ol += 1
    s["O"] = ol
    s["X"] = xl
    return s


            
            
                