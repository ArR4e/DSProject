def võitja(n):
    #O loendur
    x = 0
    o = 0
    main = {}
    for i in range(4):
        for j in range(2):
            if n[i][j] == n[i][j+1] == n[i][j+2] == "X":
                x += 1
            if n[i][j] == n[i][j+1] == n[i][j+2] == "O":
                o += 1
    for i in range(2):
        for j in range(4):
            if n[i][j] == n[i+1][j] == n[i+2][j] == "X":
                x += 1
            if n[i][j] == n[i+1][j] == n[i+2][j] == "O":
                o += 1
    for i in range(2):
        for j in range(2):
            if n[i][j] == n[i+1][j+1] == n[i+2][j+2] == "X":
                x += 1
            if n[i][j+1] == n[i+1][j] == "X":
                x += 1
            if n[i][j] == n[i+1][j+1] == n[i+2][j+2] == "O":
                o += 1
            if n[i][j+1] == n[i+1][j] == "O":
                o += 1
    main["O"] = o
    main["X"] = x   
    return main
