def võitja(maatriks):
    loendur = {}
    loendur["O"] = set()
    loendur["X"] = set()
    X_loendur = 0
    O_loendur = 0
    for rida in maatriks:
        for ühik in rida:
            if ühik == "X":
                X_loendur += 1
                if maatriks[0][0]==maatriks[0][1]==maatriks[0][2]=="X":
                    loendur["X"] = X_loendur
                if maatriks[0][1]==maatriks[0][2]==maatriks[0][3]=="X":
                    loendur["X"] = X_loendur
            if ühik == "O":
                O_loendur += 1
                if maatriks[0][0]==maatriks[0][1]==maatriks[0][2]=="O":
                    loendur["O"] = X_loendur
                if maatriks[0][1]==maatriks[0][2]==maatriks[0][3]=="O":
                    loendur["O"] = X_loendur
        print(loendur)
        
võitja([['X','O',' ','X'],
            [' ','O',' ',' '],
            [' ',' ','O',' '],
            [' ',' ',' ','O']])