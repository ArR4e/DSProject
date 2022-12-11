def võitja(maatriks):
    d = {'O': 0, 'X': 0}
    for i in range(0,len(maatriks)):
        for j in range(0,len(maatriks)):
            if maatriks[i][j:j+3] == ["O","O","O"]:
                d["O"] = d.get("O")+1
            elif maatriks[i][j:j+3] == ["X","X","X"]:
                d["X"] = d.get("X")+1
    for i in range(0,2):
        for j in range(0,2):
            if maatriks[i][j] == maatriks[i+1][j+1] == maatriks[i+2][j+2]:
                if maatriks[i][j] == "O" or maatriks[i][j] == "X":
                    d[maatriks[i][j]] = d.get(maatriks[i][j])+1
    for i in range(0,2):
        for j in range(1,3):
            if maatriks[i][-j] == maatriks[i+1][-j-1] == maatriks[i+2][-j-2]:
                if maatriks[i][-j] == "O" or maatriks[i][-j] == "X":
                    d[maatriks[i][-j]] = d.get(maatriks[i][-j])+1
    for i in range(0,2):
        for j in range(0,len(maatriks)):
            if maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j]:
                if maatriks[i][j] == "O" or maatriks[i][j] == "X":
                    d[maatriks[i][j]] = d.get(maatriks[i][j])+1
    return d
