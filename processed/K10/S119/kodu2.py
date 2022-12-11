def võitja(maatriks):
    a = {}
    xid = 0
    nullid = 0
    for rida in range(4):
        for veerg in range(2):
            if maatriks[rida][veerg] == maatriks[rida][veerg + 1] == maatriks[rida][veerg + 2] == "X":
                xid += 1
            if maatriks[rida][veerg] == maatriks[rida][veerg + 1] == maatriks[rida][veerg + 2] == "O":
                nullid += 1
    for veerg in range(4):
        for rida in range(2):
            if maatriks[rida][veerg] == maatriks[rida + 1][veerg] == maatriks[rida + 2][veerg] == "X":
                xid += 1
            if maatriks[rida][veerg] == maatriks[rida + 1][veerg] == maatriks[rida + 2][veerg] == "O":
                nullid += 1
    for rida in range(2):
        for veerg in range(3, 1, -1):
            if maatriks[veerg][rida] == maatriks[veerg - 1][rida + 1] == maatriks[veerg - 2][rida + 2] == "X":
                xid += 1
            if maatriks[veerg][rida] == maatriks[veerg - 1][rida + 1] == maatriks[veerg - 2][rida + 2] == "O":
                nullid += 1
            if maatriks[rida][veerg - 2] == maatriks[rida + 1][veerg - 1] == maatriks[rida + 2][veerg] == "X":
                xid += 1
            if maatriks[rida][veerg - 2] == maatriks[rida + 1][veerg - 1] == maatriks[rida + 2][veerg] == "O":
                nullid += 1
                
                
    a["O"] = nullid
    a["X"] = xid
    return a
print(võitja([['O',' ','O','X'],
            ['O','O','X','X'],
            ['O','X','O',' '],
            ['X','X','X','O']]))