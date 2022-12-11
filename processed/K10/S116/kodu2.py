sisend = [[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "]]

def võitja(sisend):
    counterx = 0
    countero = 0
    for i in range(len(sisend)):
        if sisend[i][0:3] == ["X","X","X"]:
            counterx += 1
        if sisend[i][1:4] == ["X","X","X"]:
            counterx += 1
            
        if sisend[i][0:3] == ["O","O","O"]:
            countero += 1
        if sisend[i][1:4] == ["O","O","O"]:
            countero += 1
        
    for j in range(len(sisend)):
        if sisend[0][j] == "X" and sisend[1][j] == "X" and sisend[2][j] == "X":
            counterx += 1
        if sisend[1][j] == "X" and sisend[2][j] == "X" and sisend[3][j] == "X":
            counterx += 1
            
        if sisend[0][j] == "O" and sisend[1][j] == "O" and sisend[2][j] == "O":
            countero += 1
        if sisend[1][j] == "O" and sisend[2][j] == "O" and sisend[3][j] == "O":
            countero += 1
            
    if sisend[1][0] == sisend[2][1] == sisend[3][2] == "X":
        counterx += 1
    if sisend[0][0] == sisend[1][1] == sisend[2][2] == "X":
        counterx += 1
    if sisend[1][1] == sisend[2][2] == sisend[3][3] == "X":
        counterx += 1
    if sisend[0][1] == sisend[1][2] == sisend[2][3] == "X":
        counterx += 1
    if sisend[1][3] == sisend[2][2] == sisend[3][1] == "X":
        counterx += 1
    if sisend[1][2] == sisend[2][1] == sisend[3][0] == "X":
        counterx += 1
    if sisend[0][3] == sisend[1][2] == sisend[2][1] == "X":
        counterx += 1
    if sisend[0][2] == sisend[1][1] == sisend[2][0] == "X":
        counterx += 1
        
        
    if sisend[1][0] == sisend[2][1] == sisend[3][2] == "O":
        countero += 1
    if sisend[0][0] == sisend[1][1] == sisend[2][2] == "O":
        countero += 1
    if sisend[1][1] == sisend[2][2] == sisend[3][3] == "O":
        countero += 1
    if sisend[0][1] == sisend[1][2] == sisend[2][3] == "O":
        countero += 1
    if sisend[1][3] == sisend[2][2] == sisend[3][1] == "O":
        countero += 1
    if sisend[1][2] == sisend[2][1] == sisend[3][0] == "O":
        countero += 1
    if sisend[0][3] == sisend[1][2] == sisend[2][1] == "O":
        countero += 1
    if sisend[0][2] == sisend[1][1] == sisend[2][0] == "O":
        countero += 1
        
    sõnastik = dict()
    sõnastik["O"] = countero
    sõnastik["X"] = counterx
    return sõnastik

print(võitja(sisend))