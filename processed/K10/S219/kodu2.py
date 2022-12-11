def võitja(maatriks):
    abilist = []
    for sisemine_list in maatriks:
        abilist.append(sisemine_list)
   
    O_loendur = 0
    X_loendur = 0
    
    tulp1 = [tulp[0] for tulp in maatriks]
    tulp2 = [tulp[1] for tulp in maatriks]
    tulp3 = [tulp[2] for tulp in maatriks]
    tulp4 = [tulp[3] for tulp in maatriks]
    tulbad_list = [tulp1, tulp2, tulp3, tulp4]
    
    diagonaal1 = [abilist[0][0], abilist[1][1], abilist[2][2]] #Peadiagonaal 1
    diagonaal2 = [abilist[1][1], abilist[2][2], abilist[3][3]] #Peadiagonaal 2
    diagonaal3 = [abilist[0][3], abilist[1][2], abilist[2][1]] #Teistpidi peadiagonaal 1
    diagonaal4 = [abilist[1][2], abilist[2][1], abilist[3][0]] #Teistpidi peadiagonaal 2
    diagonaal5 = [abilist[0][1], abilist[1][2], abilist[2][3]]
    diagonaal6 = [abilist[1][0], abilist[2][1], abilist[3][2]]
    diagonaal7 = [abilist[0][2], abilist[1][1], abilist[2][0]]
    diagonaal8 = [abilist[1][3], abilist[2][2], abilist[3][1]]
    diagonaalid_list = [diagonaal1,  diagonaal2, diagonaal3, diagonaal4, diagonaal5, diagonaal6, diagonaal7, diagonaal8]
    
    for rida in abilist:
        if rida[0] == 'X' and rida[1] == 'X' and rida[2] == 'X':
            X_loendur = X_loendur + 1
        if rida[1] == 'X' and rida[2] == 'X' and rida[3] == 'X':
            X_loendur = X_loendur + 1
    
    for rida in tulbad_list:
        if rida[0] == 'X' and rida[1] == 'X' and rida[2] == 'X':
            X_loendur = X_loendur + 1
        if rida[1] == 'X' and rida[2] == 'X' and rida[3] == 'X':
            X_loendur = X_loendur + 1

    for rida in abilist:
        if rida[0] == 'O' and rida[1] == 'O' and rida[2] == 'O':
            O_loendur = O_loendur + 1
        if rida[1] == 'O' and rida[2] == 'O' and rida[3] == 'O':
            O_loendur = O_loendur + 1
            
    for rida in tulbad_list:
        if rida[0] == 'O' and rida[1] == 'O' and rida[2] == 'O':
            O_loendur = O_loendur + 1
        if rida[1] == 'O' and rida[2] == 'O' and rida[3] == 'O':
            O_loendur = O_loendur + 1
            
    for diagonaal in diagonaalid_list:
        if diagonaal[0] == 'X' and diagonaal[1] == 'X' and diagonaal[2] == 'X':
            X_loendur = X_loendur + 1
        if diagonaal[0] == 'O' and diagonaal[1] == 'O' and diagonaal[2] == 'O':
            O_loendur = O_loendur + 1
        
    return {'O' : O_loendur, 'X' : X_loendur}