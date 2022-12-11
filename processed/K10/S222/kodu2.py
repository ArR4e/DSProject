def võitja(m):
    palju = {"O":0,"X":0}
    for n in range(4):
        for ox in ["O","X"]:
            if m[n][0:3].count(ox) == 3:
                palju[ox] += 1
            if m[n][1:5].count(ox) == 3:
                palju[ox] += 1
            if m[0][n] == m[1][n] == m[2][n] == ox:
                palju[ox] += 1
            if m[1][n] == m[2][n] == m[3][n] == ox:
                palju[ox] += 1
    for ox in ["O","X"]:
        if m[0][2] == m[1][1] == m[2][0] == ox:
            palju[ox] += 1
        if m[0][1] == m[1][2] == m[2][3] == ox:
            palju[ox] += 1
        if m[1][0] == m[2][1] == m[3][2] == ox:
            palju[ox] += 1
        if m[1][3] == m[2][2] == m[3][1] == ox:
            palju[ox] += 1
        if m[0][0] == m[1][1] == m[2][2] == ox:
            palju[ox] += 1
        if m[1][1] == m[2][2] == m[3][3] == ox:
            palju[ox] += 1
        if m[0][3] == m[1][2] == m[2][1] == ox:
            palju[ox] += 1
        if m[1][2] == m[2][1] == m[3][0] == ox:
            palju[ox] += 1
    return palju
print(võitja([["O","O","O","O"],["O","O","O","O"],["O","O","O","O"],["O","O","O","O"]]))