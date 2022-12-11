asjad = [[' ', 'O', 'X', ' '], ['O', 'X', 'O', 'X'], ['X', 'O', 'X', 'O'], [' ', 'X', 'O', ' ']]

def võitja(maatriks):
    mitux = 0
    mituo = 0
    for i in range(len(maatriks)):
        for j in range(len(maatriks)-2):
            if maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2]:
                if maatriks[i][j] == "X":
                    mitux += 1
                elif maatriks[i][j] == "O":
                    mituo += 1
    for i in range(len(maatriks)-2):
        for j in range(len(maatriks)):
            if maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j]:
                if maatriks[i][j] == "X":
                    mitux += 1
                elif maatriks[i][j] == "O":
                    mituo += 1
    for i in range(len(maatriks)-2):
        for j in range(len(maatriks)-2):
            if maatriks[i][j] == maatriks[i+1][j+1] == maatriks[i+2][j+2]:
                if maatriks[i][j] == "X":
                    mitux += 1
                elif maatriks[i][j] == "O":
                    mituo += 1
    for i in range(len(maatriks)-2):
        for j in range(3, len(maatriks)):
            if maatriks[i][j] == maatriks[i+1][j-1] == maatriks[i+2][j-2]:
                if maatriks[i][j] == "X":
                    mitux += 1
                elif maatriks[i][j] == "O":
                    mituo += 1
    for i in range(len(maatriks)-2):
        for j in range(-2, -1):
            if maatriks[i][j] == maatriks[i+1][j-1] == maatriks[i+2][j-2]:
                if maatriks[i][j] == "X":
                    mitux += 1
                elif maatriks[i][j] == "O":
                    mituo += 1
    return {"O" : mituo, "X" : mitux}

print(võitja(asjad))