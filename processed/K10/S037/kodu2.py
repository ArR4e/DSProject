def võitja(maatriks):
    loendur = {}
    loendur['O'] = 0
    loendur['X'] = 0
    i = 0
    for rida in maatriks: #rida paremalt vasakule + rida vasakult paremale
        if rida[0] == rida[1] == rida[2] == 'X': 
            loendur['X'] = loendur.get('X',0) + 1
        if rida[-1] == rida[-2] == rida[-3] == 'X': 
            loendur['X'] = loendur.get('X',0) + 1
        if rida[0] == rida[1] == rida[2] == 'O':
            loendur['O'] = loendur.get('O',0) + 1
        if rida[-1] == rida[-2] == rida[-3] == 'O':
            loendur['O'] = loendur.get('O',0) + 1
    
    while i < 4: #veerg ülevalt alla ja alt üles
        if maatriks[0][i] == maatriks[1][i] == maatriks[2][i] == 'X':
            loendur['X'] = loendur.get('X',0) + 1
        if maatriks[3][i] == maatriks[2][i] == maatriks[1][i] == 'X':
            loendur['X'] = loendur.get('X',0) + 1
        if maatriks[0][i] == maatriks[1][i] == maatriks[2][i] == 'O':
            loendur['O'] = loendur.get('O',0) + 1
        if maatriks[3][i] == maatriks[2][i] == maatriks[1][i] == 'O':
            loendur['O'] = loendur.get('O',0) + 1
        i += 1
                
    if maatriks[0][0] ==  maatriks[1][1] == maatriks[2][2] == 'X': #diagonaal1 edasi-tagasi
        loendur['X'] = loendur.get('X',0) + 1
    if maatriks[3][3] ==  maatriks[2][2] == maatriks[1][1] == 'X':
        loendur['X'] = loendur.get('X',0) + 1
    if maatriks[0][0] ==  maatriks[1][1] == maatriks[2][2] == 'O':
        loendur['O'] = loendur.get('O',0) + 1
    if maatriks[3][3] ==  maatriks[2][2] == maatriks[1][1] == 'O':
        loendur['O'] = loendur.get('O',0) + 1
                
    if maatriks[0][-1] ==  maatriks[1][2] == maatriks[2][1] == 'X': #diagonaal2 edasi-tagasi
        loendur['X'] = loendur.get('X',0) + 1
    if maatriks[3][0] ==  maatriks[2][1] == maatriks[1][2] == 'X':
        loendur['X'] = loendur.get('X',0) + 1
    if maatriks[0][-1] ==  maatriks[1][2] == maatriks[2][1] == 'O':
        loendur['O'] = loendur.get('O',0) + 1
    if maatriks[3][0] ==  maatriks[2][1] == maatriks[1][2] == 'O':
        loendur['O'] = loendur.get('O',0) + 1

    if maatriks[2][0] ==  maatriks[1][1] == maatriks[0][2] == 'X': #väiksemad diagonaalid edasi-tagasi
        loendur['X'] = loendur.get('X',0) + 1
    if maatriks[2][0] ==  maatriks[1][1] == maatriks[0][2] ==  'O':
        loendur['O'] = loendur.get('O',0) + 1
    if maatriks[3][1] ==  maatriks[2][2] == maatriks[1][3] == 'X': 
        loendur['X'] = loendur.get('X',0) + 1
    if maatriks[3][1] ==  maatriks[2][2] == maatriks[1][3] == 'O':
        loendur['O'] = loendur.get('O',0) + 1
    if maatriks[1][0] ==  maatriks[2][1] == maatriks[3][2] == 'X': 
        loendur['X'] = loendur.get('X',0) + 1
    if maatriks[1][0] ==  maatriks[2][1] == maatriks[3][2] ==  'O':
        loendur['O'] = loendur.get('O',0) + 1
    if maatriks[0][1] ==  maatriks[1][2] == maatriks[2][3] == 'X':
        loendur['O'] = loendur.get('O',0) + 1
    if maatriks[0][1] ==  maatriks[1][2] == maatriks[2][3] == 'O':
        loendur['O'] = loendur.get('O',0) + 1 

    return(loendur)