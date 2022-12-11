def võitja(järjend):
    X_väärtus = 0
    X_vertikaalne = 0 #1. veerg
    X_vertikaalne1 = 0#2. veerg
    X_vertikaalne2 = 0#3. veerg
    X_vertikaalne3 = 0#4. veerg
    X_diagonaalis = 0
    X_diagonaalis1 = 0
    X_diagonaalis2 = 0
    
    Vastus = {}
    O_vertikaalne = 0
    O_vertikaalne1 = 0
    O_vertikaalne2 = 0
    O_vertikaalne3 = 0
    O_diagonaalis = 0
    O_diagonaalis1 = 0
    O_diagonaalis2 = 0
    O_väärtus = 0
    a = 0
    loopide_arv = 0

    for i in järjend:
        if i[0] == "X" and i[1] == "X" and i[2] =="X": #Horisontaalis 
             X_väärtus += 1
        elif i[1] == "X" and i[2] == "X" and i[3] =="X":
             X_väärtus += 1
             
        if i[a] == "X": #Vertikaalis
            X_vertikaalne += 1
        elif i[a] != "X":
            X_vertikaalne = 0
            
        if i[1] == "X":
            X_vertikaalne1 += 1
        elif i[1] != "X":
            X_vertikaalne1 = 0
        if i[2] == "X":
            X_vertikaalne2 += 1
        elif i[2] != "X":
            X_vertikaalne2 = 0
        if i[3] == "X":
            X_vertikaalne3 += 1
        elif i[3] != "X":
            X_vertikaalne3 = 0
            
            
        if X_vertikaalne == 3:
            X_väärtus += 1
        if X_vertikaalne1 == 3:
            X_väärtus += 1
        if X_vertikaalne2 == 3:
            X_väärtus += 1
        if X_vertikaalne3 == 3:
            X_väärtus += 1
        
        
        
        if i[0] == "O" and i[1] == "O" and i[2] =="O": #Horisontaalis 
             O_väärtus += 1
        elif i[1] == "O" and i[2] == "O" and i[3] =="O":
             O_väärtus += 1
             
        if i[a] == "O": #Vertikaalis
            O_vertikaalne += 1
        elif i[a] != "O":
            O_vertikaalne = 0
            
        if i[1] == "O":
            O_vertikaalne1 += 1
        elif i[1] != "O":
            O_vertikaalne1 = 0
        if i[2] == "O":
            O_vertikaalne2 += 1
        elif i[2] != "O":
            O_vertikaalne2 = 0
        if i[3] == "O":
            O_vertikaalne3 += 1
        elif i[3] != "O":
            O_vertikaalne3 = 0
            
            
        if O_vertikaalne == 3:
            O_väärtus += 1
        if O_vertikaalne1 == 3:
            O_väärtus += 1
        if O_vertikaalne2 == 3:
            O_väärtus += 1
        if O_vertikaalne3 == 3:
            O_väärtus += 1
        if loopide_arv == 0:
            if i[0] == "X":
                X_diagonaalis += 1
            if i[1] == "X":
                X_diagonaalis1 += 1
        if loopide_arv == 1:
            if i[1] == "X":
                X_diagonaalis += 1
            if i[2] == "X":
                X_diagonaalis1 += 1
            if i[0] == "X":
                X_diagonaalis2 += 1
        if loopide_arv == 2:
            if i[2] == "X":
                X_diagonaalis += 1
            if i[3] == "X":
                X_diagonaalis1 += 1
            if i[1] == "X":
                X_diagonaalis2 += 1
        if loopide_arv == 3:
            if i[2] == "X":
                X_diagonaalis2 += 1
        if X_diagonaalis == 3:
            X_väärtus += 1
            X_diagonaalis = 0
        if X_diagonaalis1 == 3:
            X_väärtus += 1
            X_diagonaalis1 = 0
        if X_diagonaalis2 == 3:
            X_väärtus += 1
            X_diagonaalis2 = 0
        
        
        if loopide_arv == 0:
            if i[0] == "O":
                O_diagonaalis += 1
            if i[1] == "O":
                O_diagonaalis1 += 1
        if loopide_arv == 1:
            if i[1] == "O":
                O_diagonaalis += 1
            if i[2] == "O":
                O_diagonaalis1 += 1
            if i[0] == "O":
                O_diagonaalis2 += 1
        if loopide_arv == 2:
            if i[2] == "O":
                O_diagonaalis += 1
            if i[3] == "O":
                O_diagonaalis1 += 1
            if i[1] == "O":
                O_diagonaalis2 += 1
        if loopide_arv == 3:
            if i[2] == "O":
                O_diagonaalis2 += 1
        if O_diagonaalis == 3:
            O_väärtus += 1
            O_diagonaalis = 0
        if O_diagonaalis1 == 3:
            O_väärtus += 1
            O_diagonaalis1 = 0
        if O_diagonaalis2 == 3:
            O_väärtus += 1
            O_diagonaalis2 = 0
        loopide_arv += 1
            
        
        
        
        
            
    Vastus["X"] = X_väärtus
    Vastus["O"] = O_väärtus
    return Vastus
# võitja([['X',' ',' ',' '],
#         ['X',' ','X',' '],
#         [' ','X',' ','X'],
#         [' ','O','X',' ']])
