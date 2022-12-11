def võitja(ttt):
    tulemus = {"O" : 0, "X" : 0}
    # Horisontaal kontroll
    for i in range(4):
        for j in range(2):
            if ttt[i][j] == "O":
                if ttt[i][j+1] == "O" and ttt[i][j+2] == "O":
                    tulemus["O"] += 1
            elif ttt[i][j] == "X":
                if ttt[i][j+1] == "X" and ttt[i][j+2] == "X":
                    tulemus["X"] += 1
    # Vertikaal kontroll
    for i in range(2):
        for j in range(4):
            if ttt[i][j] == "O":
                if ttt[i+1][j] == "O" and ttt[i+2][j] == "O":
                    tulemus["O"] += 1
            elif ttt[i][j] == "X":
                if ttt[i+1][j] == "X" and ttt[i+2][j] == "X":
                    tulemus["X"] += 1
    # Diagonaal kontroll
    for i in range(2):
        for j in range(4):
                if j < 2:
                    if ttt[i][j] == "O":
                        if ttt[i+1][j+1] == "O" and ttt[i+2][j+2] == "O":
                            tulemus["O"] += 1
                    elif ttt[i][j] == "X":
                        if ttt[i+1][j+1] == "X" and ttt[i+2][j+2] == "X":
                            tulemus["X"] += 1
                else:
                    if ttt[i][j] == "O":
                        if ttt[i+1][j-1] == "O" and ttt[i+2][j-2] == "O":
                            tulemus["O"] += 1
                    elif ttt[i][j] == "X":
                        if ttt[i+1][j-1] == "X" and ttt[i+2][j-2] == "X":
                            tulemus["X"] += 1
                
    return tulemus
print(võitja([['X','X','O','X'],
              ['O','O','X','O'],
              ['O','X','O','X'],
              ['X','O','X','O']]))                