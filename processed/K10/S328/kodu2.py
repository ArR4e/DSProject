def võitja(maatriks):
    sõnastik = {"O": 0, "X": 0}
    if len(maatriks) == 4:
        for rida in range(4):
            for veerg in range(4):
                try:
                    if maatriks[rida][veerg] == "X":
                        if maatriks[rida + 1][veerg + 1] == "X" and maatriks[rida + 2][veerg + 2] == "X":
                            sõnastik["X"] += 1
                        elif maatriks[rida][veerg + 1] == "X" and maatriks[rida][veerg + 2] == "X":
                            sõnastik["X"] += 1
                        elif maatriks[rida + 1][veerg] == "X" and maatriks[rida + 2][veerg] == "X":
                            sõnastik["X"] += 1
                        elif maatriks[rida + 1][veerg - 1] == "X" and maatriks[rida + 2][veerg - 2] == "X":
                            sõnastik["X"] += 1
                            
                    elif maatriks[rida][veerg] == "O":
                        if maatriks[rida + 1][veerg + 1] == "O" and maatriks[rida + 2][veerg + 2] == "O":
                            sõnastik["O"] += 1
                        elif maatriks[rida][veerg + 1] == "O" and maatriks[rida][veerg + 2] == "O":
                            sõnastik["O"] += 1
                        elif maatriks[rida + 1][veerg] == "O" and maatriks[rida + 2][veerg] == "O":
                            sõnastik["O"] += 1
                        elif maatriks[rida + 1][veerg - 1] == "O" and maatriks[rida + 2][veerg - 2] == "O":
                            sõnastik["O"] += 1
                except:
                    continue
    return sõnastik
    

print(võitja([['O',' ',' ','X'],
              [' ','O','X',' '],
              [' ','X','O',' '],
              ['X',' ',' ','O']]))
    
    