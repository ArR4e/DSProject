def read(x):
    x_punktid = 0
    o_punktid = 0

    for rida in x:
        if rida[0:3] == ["X", "X", "X"]:
            x_punktid += 1
        if rida[1:4] == ["X", "X", "X"]:
            x_punktid += 1
        if rida[0:3] == ["O", "O", "O"]:
            o_punktid += 1
        if rida[1:4] == ["O", "O", "O"]:
            o_punktid += 1
    
    return [o_punktid, x_punktid]

def veerud(x):
    transponeeritud = [
    [' ',' ',' ',' '],
    [' ',' ',' ',' '],
    [' ',' ',' ',' '],
    [' ',' ',' ',' ']]

    for i in range(len(x)):
        for j in range(len(x[0])):
            transponeeritud[j][i] = x[i][j]
       
    return read(transponeeritud)

def diagonaalid_vasak(x):
    x_punktid = 0
    o_punktid = 0

    ül_dg = [x[0][1], x[1][2], x[2][3]]
    kesk_dg = [x[0][0], x[1][1], x[2][2], x[3][3]]
    al_dg = [x[1][0], x[2][1], x[3][2]]

    if ül_dg[0] == ül_dg[1] == ül_dg[2]:
        if ül_dg[0] == "X":
            x_punktid += 1
        elif ül_dg[0] == "O":
            o_punktid += 1

    if al_dg[0] == al_dg[1] == al_dg[2]:
        if al_dg[0] == "X":
            x_punktid += 1
        elif al_dg[0] == "O":
            o_punktid += 1
            
    if kesk_dg[0] == kesk_dg[1] == kesk_dg[2]:
        if kesk_dg[0] == "X":
            x_punktid += 1
        elif kesk_dg[0] == "O":
            o_punktid += 1

    if kesk_dg[1] == kesk_dg[2] == kesk_dg[3]:
        if kesk_dg[1] == "X":
            x_punktid += 1
        elif kesk_dg[1] == "O":
            o_punktid += 1
            
    return [o_punktid, x_punktid]

def diagonaalid_parem(x):
    x_punktid = 0
    o_punktid = 0

    ül_dg = [x[0][2], x[1][1], x[2][0]]
    kesk_dg = [x[0][3], x[1][2], x[2][1], x[3][0]]
    al_dg = [x[1][3], x[2][2], x[3][1]]
    
    if ül_dg[0] == ül_dg[1] == ül_dg[2]:
        if ül_dg[0] == "X":
            x_punktid += 1
        elif ül_dg[0] == "O":
            o_punktid += 1

    if al_dg[0] == al_dg[1] == al_dg[2]:
        if al_dg[0] == "X":
            x_punktid += 1
        elif al_dg[0] == "O":
            o_punktid += 1
            
    if kesk_dg[0] == kesk_dg[1] == kesk_dg[2]:
        if kesk_dg[0] == "X":
            x_punktid += 1
        elif kesk_dg[0] == "O":
            o_punktid += 1

    if kesk_dg[1] == kesk_dg[2] == kesk_dg[3]:
        if kesk_dg[1] == "X":
            x_punktid += 1
        elif kesk_dg[1] == "O":
            o_punktid += 1
    
    return [o_punktid, x_punktid]

def võitja(x):
    pr = read(x)
    pv = veerud(x)
    pdgv = diagonaalid_vasak(x)
    pdgp = diagonaalid_parem(x)
    
    o_punktid_kokku = pr[0] + pv[0] + pdgv[0] + pdgp[0]
    x_punktid_kokku = pr[1] + pv[1] + pdgv[1] + pdgp[1]
    
    punktid = {}
    punktid["O"] = o_punktid_kokku
    punktid["X"] = x_punktid_kokku
    
    return punktid