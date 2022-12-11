def võitja(maatriks):
    O_punktid=0   
    X_punktid=0
    seis={}
        #horisontaalselt
    if maatriks[0][0] == 'O' and maatriks[0][1] == 'O' and maatriks[0][2] == 'O':
        O_punktid += 1
    if maatriks[0][1] == 'O' and maatriks[0][2] == 'O' and maatriks[0][3] == 'O':
        O_punktid += 1
    if maatriks[1][0] == 'O' and maatriks[1][1] == 'O' and maatriks[1][2] == 'O':
        O_punktid += 1
    if maatriks[1][1] == 'O' and maatriks[1][2] == 'O' and maatriks[1][3] == 'O':
        O_punktid += 1
    if maatriks[2][0] == 'O' and maatriks[2][1] == 'O' and maatriks[2][2] == 'O':
        O_punktid += 1
    if maatriks[2][1] == 'O' and maatriks[2][2] == 'O' and maatriks[2][3] == 'O':
        O_punktid += 1
    if maatriks[3][0] == 'O' and maatriks[3][1] == 'O' and maatriks[3][2] == 'O':
        O_punktid += 1
    if maatriks[3][1] == 'O' and maatriks[3][2] == 'O' and maatriks[3][3] == 'O':
        O_punktid += 1
            
        #vertikaalselt
    if maatriks[0][0] == 'O' and maatriks[1][0] == 'O' and maatriks[2][0] == 'O':
        O_punktid += 1
    if maatriks[1][0] == 'O' and maatriks[2][0] == 'O' and maatriks[3][0] == 'O':
        O_punktid += 1
    if maatriks[0][1] == 'O' and maatriks[1][1] == 'O' and maatriks[2][1] == 'O':
        O_punktid += 1
    if maatriks[1][1] == 'O' and maatriks[2][1] == 'O' and maatriks[3][1] == 'O':
        O_punktid += 1
    if maatriks[0][2] == 'O' and maatriks[1][2] == 'O' and maatriks[2][2] == 'O':
        O_punktid += 1
    if maatriks[1][2] == 'O' and maatriks[2][2] == 'O' and maatriks[3][2] == 'O':
        O_punktid += 1
    if maatriks[0][3] == 'O' and maatriks[1][3] == 'O' and maatriks[2][3] == 'O':
        O_punktid += 1
    if maatriks[1][3] == 'O' and maatriks[2][3] == 'O' and maatriks[3][3] == 'O':
        O_punktid += 1
            
            #vasakult-paremale diagonaalselt
    if maatriks[0][0] == 'O' and maatriks[1][1] == 'O' and maatriks[2][2] == 'O':
        O_punktid += 1
    if maatriks[1][1] == 'O' and maatriks[2][2] == 'O' and maatriks[3][3] == 'O':
        O_punktid += 1
    if maatriks[0][1] == 'O' and maatriks[1][2] == 'O' and maatriks[2][3] == 'O':
        O_punktid += 1
    if maatriks[1][0] == 'O' and maatriks[2][1] == 'O' and maatriks[3][2] == 'O':
        O_punktid += 1

        #paremalt-vasakule diagonaalselt
    if maatriks[0][3] == 'O' and maatriks[1][2] == 'O' and maatriks[2][1] == 'O':
        O_punktid += 1
    if maatriks[1][2] == 'O' and maatriks[2][1] == 'O' and maatriks[3][0] == 'O':
        O_punktid += 1
    if maatriks[0][2] == 'O' and maatriks[1][1] == 'O' and maatriks[2][0] == 'O':
        O_punktid += 1
    if maatriks[1][3] == 'O' and maatriks[2][2] == 'O' and maatriks[3][1] == 'O':
        O_punktid += 1

###############################################################################
        
                #horisontaalselt
    if maatriks[0][0] == 'X' and maatriks[0][1] == 'X' and maatriks[0][2] == 'X':
        X_punktid += 1
    if maatriks[0][1] == 'X' and maatriks[0][2] == 'X' and maatriks[0][3] == 'X':
        X_punktid += 1
    if maatriks[1][0] == 'X' and maatriks[1][1] == 'X' and maatriks[1][2] == 'X':
        X_punktid += 1
    if maatriks[1][1] == 'X' and maatriks[1][2] == 'X' and maatriks[1][3] == 'X':
        X_punktid += 1
    if maatriks[2][0] == 'X' and maatriks[2][1] == 'X' and maatriks[2][2] == 'X':
        X_punktid += 1
    if maatriks[2][1] == 'X' and maatriks[2][2] == 'X' and maatriks[2][3] == 'X':
        X_punktid += 1
    if maatriks[3][0] == 'X' and maatriks[3][1] == 'X' and maatriks[3][2] == 'X':
        X_punktid += 1
    if maatriks[3][1] == 'X' and maatriks[3][2] == 'X' and maatriks[3][3] == 'X':
        X_punktid += 1
            
        #vertikaalselt
    if maatriks[0][0] == 'X' and maatriks[1][0] == 'X' and maatriks[2][0] == 'X':
        X_punktid += 1
    if maatriks[1][0] == 'X' and maatriks[2][0] == 'X' and maatriks[3][0] == 'X':
        X_punktid += 1
    if maatriks[0][1] == 'X' and maatriks[1][1] == 'X' and maatriks[2][1] == 'X':
        X_punktid += 1
    if maatriks[1][1] == 'X' and maatriks[2][1] == 'X' and maatriks[3][1] == 'X':
        X_punktid += 1
    if maatriks[0][2] == 'X' and maatriks[1][2] == 'X' and maatriks[2][2] == 'X':
        X_punktid += 1
    if maatriks[1][2] == 'X' and maatriks[2][2] == 'X' and maatriks[3][2] == 'X':
        X_punktid += 1
    if maatriks[0][3] == 'X' and maatriks[1][3] == 'X' and maatriks[2][3] == 'X':
        X_punktid += 1
    if maatriks[1][3] == 'X' and maatriks[2][3] == 'X' and maatriks[3][3] == 'X':
        X_punktid += 1
            
            #vasakult-paremale diagonaalselt
    if maatriks[0][0] == 'X' and maatriks[1][1] == 'X' and maatriks[2][2] == 'X':
        X_punktid += 1
    if maatriks[1][1] == 'X' and maatriks[2][2] == 'X' and maatriks[3][3] == 'X':
        X_punktid += 1
    if maatriks[0][1] == 'X' and maatriks[1][2] == 'X' and maatriks[2][3] == 'X':
        X_punktid += 1
    if maatriks[1][0] == 'X' and maatriks[2][1] == 'X' and maatriks[3][2] == 'X':
        X_punktid += 1

        #paremalt-vasakule diagonaalselt
    if maatriks[0][3] == 'X' and maatriks[1][2] == 'X' and maatriks[2][1] == 'X':
        X_punktid += 1
    if maatriks[1][2] == 'X' and maatriks[2][1] == 'X' and maatriks[3][0] == 'X':
        X_punktid += 1
    if maatriks[0][2] == 'X' and maatriks[1][1] == 'X' and maatriks[2][0] == 'X':
        X_punktid += 1
    if maatriks[1][3] == 'X' and maatriks[2][2] == 'X' and maatriks[3][1] == 'X':
        X_punktid += 1
    
    seis['O'] = O_punktid
    seis['X'] = X_punktid

    return seis