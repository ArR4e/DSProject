def võitja(mat):
    Xarv = 0
    Oarv = 0
    vastus = {}
    for i in range(4):
        for j in range(2):
            if mat[i][j] == mat[i][j+1] == mat[i][j+2] == "X":
                Xarv += 1
            elif mat[i][j] == mat[i][j+1] == mat[i][j+2] == "O":
                Oarv += 1
    for i in range(2):
        for j in range(4):
            if mat[i][j] == mat[i+1][j] == mat[i+2][j] == "X":
                Xarv += 1
            elif mat[i][j] == mat[i+1][j] == mat[i+2][j] == "O":
                Oarv += 1
    for i in range(2):
        for j in range(2):
            if mat[i][j] == mat[i+1][j+1] == mat[i+2][j+2]== "X":
                Xarv += 1
            elif mat[i][j] == mat[i+1][j+1] == mat[i+2][j+2]== "O":
                Oarv += 1
            if mat[i+2][j] == mat[i+1][j+1] == mat[i][j+2]== "X":
                Xarv += 1
            elif mat[i+2][j] == mat[i+1][j+1] == mat[i][j+2]== "O":
                Oarv += 1
    vastus["X"] = Xarv
    vastus["O"] = Oarv
    return vastus
