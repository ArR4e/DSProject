def võitja(maatriks):
    XOXO = {"O" : 0, "X" : 0}
    for rida in maatriks:
        if rida.count("X") == 4:
            XOXO["X"] += 2
        elif rida.count("X") == 3:
            XOXO["X"] += 1
        if rida.count("O") == 4:
            XOXO["O"] += 2
        elif rida.count("O") == 3:
            XOXO["O"] += 1
    for veeru_index in range(len(maatriks[0])):
        veerg = [rida[veeru_index] for rida in maatriks]
        if veerg.count("X") == 4:
            XOXO["X"] += 2
        elif veerg.count("X") == 3:
            XOXO["X"] += 1
        if veerg.count("O") == 4:
            XOXO["O"] += 2
        elif veerg.count("O") == 3:
            XOXO["O"] += 1
    for i in range(2):
        if maatriks[0 + i][0] == maatriks[1 + i][1] == maatriks[2 + i][2] == "X":
            XOXO["X"] += 1
        elif maatriks[0 + i][0] == maatriks[1 + i][1] == maatriks[2 + i][2] == "O":
            XOXO["O"] += 1
        if maatriks[0 + i][1] == maatriks[1 + i][2] == maatriks[2 + i][3] == "X":
            XOXO["X"] += 1
        elif maatriks[0 + i][1] == maatriks[1 + i][2] == maatriks[2 + i][3] == "O":
            XOXO["O"] += 1
        if maatriks[0 + i][3] == maatriks[1 + i][2] == maatriks[2 + i][1] == "X":
            XOXO["X"] += 1
        elif maatriks[0 + i][3] == maatriks[1 + i][2] == maatriks[2 + i][1] == "O":
            XOXO["O"] += 1
        if maatriks[0 + i][2] == maatriks[1 + i][1] == maatriks[2 + i][0] == "X":
            XOXO["X"] += 1
        elif maatriks[0 + i][2] == maatriks[1 + i][1] == maatriks[2 + i][0] == "O":
            XOXO["O"] += 1
    
    return XOXO