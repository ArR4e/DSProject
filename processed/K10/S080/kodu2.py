def võitja(maatriks):
    indexr = 0
    indexe = 0
    sõnastik = {}
   
    o = 0
    x = 0
        #if maatriks[0][0] == 'O' and maatriks[1][1] == 'O' and maatriks[2][2] == 'O' and maatriks[3][3]== 'O' or maatriks[0][3] == 'O' and maatriks[1][2] == 'O' and maatriks[2][1] == 'O' and maatriks[1][0]== 'O':
         #   o = o + 2

    if maatriks[0][0] == 'O' and maatriks[1][1] == 'O' and maatriks[2][2] == 'O': 
        o = o + 1
    if maatriks[0][1] == 'O' and maatriks[1][2] == 'O' and maatriks[2][3] == 'O':
        o = o + 1
    if maatriks[1][1] == 'O' and maatriks[2][2] == 'O' and maatriks[3][3] == 'O':
        o = o + 1
    if maatriks[0][3] == 'O' and maatriks[1][2] == 'O' and maatriks[2][1] == 'O':
        o = o + 1
    if maatriks[0][2] == 'O' and maatriks[1][1] == 'O' and maatriks[2][0] == 'O':
        o = o + 1
    if maatriks[1][3] == 'O' and maatriks[2][2] == 'O' and maatriks[3][1] == 'O':
        o = o + 1
    if maatriks[0][0] == 'X' and maatriks[1][1] == 'X' and maatriks[2][2] == 'X': 
        x = x + 1
    if maatriks[0][1] == 'X' and maatriks[1][2] == 'X' and maatriks[2][3] == 'X':
        x = x + 1
    if maatriks[1][1] == 'X' and maatriks[2][2] == 'X' and maatriks[3][3] == 'x':
        x = x + 1
    if maatriks[0][3] == 'X' and maatriks[1][2] == 'X' and maatriks[2][1] == 'X':
        x = x + 1
    if maatriks[0][2] == 'X' and maatriks[1][1] == 'X' and maatriks[2][0] == 'X':
        x = x + 1
    if maatriks[1][3] == 'X' and maatriks[2][2] == 'X' and maatriks[3][1] == 'X':
        x = x + 1
    
    while True:
        if maatriks[0][0]=='O' and maatriks[0][1]== 'O' and maatriks[0][2] == 'O' and maatriks[0][3] == 'O':
            o = o+2
            maatriks.pop(0)
        elif  maatriks[0][0]=='O' and maatriks[0][1]== 'O' and maatriks[0][2] == 'O'or maatriks[0][1]=='O' and maatriks[0][2]== 'O' and maatriks[0][3] == 'O':
            x = x + 1
            maatriks.pop(0)
        elif maatriks[0][0]=='X' and maatriks[0][1]== 'X' and maatriks[0][2] == 'X' and maatriks[0][3] == 'X':
            x = x + 2
            maatriks.pop(0)
        elif  maatriks[0][0]=='X' and maatriks[0][1]== 'X' and maatriks[0][2] == 'X'or maatriks[0][1]=='X' and maatriks[0][2]== 'X' and maatriks[0][3] == 'X':
            x = x + 1
            maatriks.pop(0)
        if maatriks[0] == '' :
            break
        
    sõnastik['O'] = o
    sõnastik['X'] = x

    return sõnastik
    
        

            