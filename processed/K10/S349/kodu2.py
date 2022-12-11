def võitja(maatriks):
    
    X_sümbol = 0
    O_sümbol = 0
            
    # vasakult-paremale
    for järjend in range(4):
        for vastus in range(2):
            if maatriks[järjend][vastus]==maatriks[järjend][vastus +1]==maatriks[järjend][vastus+2] == "X":
                X_sümbol += 1
            elif maatriks[järjend][vastus]==maatriks[järjend][vastus +1]==maatriks[järjend][vastus+2] == "O":
                O_sümbol += 1
        
    # ülevalt-alla
    for järjend in range(2):
        for vastus in range(4):
            if maatriks[järjend][vastus]==maatriks[järjend +1][vastus]==maatriks[järjend+2][vastus] == "X":
                X_sümbol += 1
            elif maatriks[järjend][vastus]==maatriks[järjend+1][vastus]==maatriks[järjend+2][vastus] == "O":
                O_sümbol += 1
                
    #vasakult paremale diagonaalis
    for järjend in range(2):
        for vastus in range(2):
            if maatriks[järjend][vastus]==maatriks[järjend +1][vastus+1]==maatriks[järjend+2][vastus+2] == "X":
                X_sümbol += 1
            elif maatriks[järjend][vastus]==maatriks[järjend+1][vastus+1]==maatriks[järjend+2][vastus+2] == "O":
                O_sümbol += 1
                
    #kõrvaldiagonaal - alt vasakult paremale
    for järjend in range(2):
        for vastus in range(3,5):
            if maatriks[järjend][vastus-1]==maatriks[järjend+1][vastus-2]==maatriks[järjend+2][vastus-3] == "X":
                X_sümbol += 1
            elif maatriks[järjend][vastus-1]==maatriks[järjend+1][vastus-2]==maatriks[järjend+2][vastus-3] == "O":
                O_sümbol += 1
                
    sõnastik = {"X":X_sümbol, "O":O_sümbol}

    return sõnastik

print(võitja([['O',' ','O','X'],
            ['O','O','X','X'],
            ['O','X','O',' '],
            ['X','X','X','O']]))
