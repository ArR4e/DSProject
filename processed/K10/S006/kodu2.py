def võitja(maatriks):
    X_loendur = 0
    O_loendur = 0
    for element in maatriks:
        if element.count("O") == 4:
            O_loendur += 2
        elif element.count("O") == 3:
            if element[0] == " " or element[0] == "X":
                O_loendur += 1
            elif element[3] == " " or element[3] == "X":
                O_loendur += 1
            else:
                O_loendur += 0
        elif element.count("X") == 4:
            X_loendur += 2
        elif element.count("X") == 3:
            if element[0] == " " or element[0] == "O":
                X_loendur += 1
            elif element[3] == " " or element[3] == "O":
                X_loendur += 1
            else:
                X_loendur += 0
    for element in range(2):
        for element2 in range(4):
            if maatriks[element][element2] == maatriks[element + 1][element2] == \
               maatriks[element + 2][element2] == "O":
                O_loendur += 1
            elif maatriks[element][element2] == maatriks[element + 1][element2] == \
               maatriks[element + 2][element2] == "X":
                X_loendur += 1
    for element in range(2):
        for element2 in range(2):
            if maatriks[element][element2] == maatriks[element + 1][element2 + 1] == \
               maatriks[element + 2][element2 + 2] == "O":
                O_loendur += 1
            elif maatriks[element][element2] == maatriks[element + 1][element2 + 1] == \
               maatriks[element + 2][element2 + 2] == "X":
                X_loendur += 1
    for element in range(2):
        for element2 in range(2):
            if maatriks[element][element2 + 2] == maatriks[element + 1][element2 + 1] == \
               maatriks[element + 2][element2] == "O":
                O_loendur += 1
            elif maatriks[element][element2 + 2] == maatriks[element + 1][element2 + 1] == \
               maatriks[element + 2][element2] == "X":
                X_loendur += 1
    tagastus = {"X": X_loendur, "O": O_loendur}
    return tagastus
     


# maatriks = [["X", "O", "X", "O"],
#             ["X", "X", "X", "O"],
#             ["X", "X", "X", "O"],
#             ["X", "O", "X", "X"]]
# võitja(maatriks)