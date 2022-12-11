def võitja(maatriks):
    vastus = {}
    ovaste = 0
    xvaste = 0
    järjend = []
    for el in maatriks:
        if ['O', 'O', 'O', ' '] == el or ['O', 'O', 'O', 'O'] == el or [' ', 'O', 'O', 'O'] == el:
            ovaste += 1
        elif ['X', 'X', 'X', ' '] == el or [' ', 'X', 'X', 'X'] == el or ['X', 'X', 'X', 'X'] == el:
            xvaste += 1
        if ['O', 'O', 'O', 'X'] == el or ['O', 'O', 'O', 'O'] == el or ['X', 'O', 'O', 'O'] == el:
            ovaste += 1
        elif ['X', 'X', 'X', 'O'] == el or ['O', 'X', 'X', 'X'] == el or ['X', 'X', 'X', 'X'] == el:
            xvaste += 1
        for täht in el:
            järjend += [täht]
    i = 0        
    while i < 4:
        if ['O', 'O', 'O', ' '] == järjend[i::4] or ['O', 'O', 'O', 'O'] == järjend[i::4] or [' ', 'O', 'O', 'O'] == järjend[i::4]:
            ovaste+=1
        elif ['X', 'X', 'X', ' '] == järjend[i::4] or [' ', 'X', 'X', 'X'] == järjend[i::4] or ['X', 'X', 'X', 'X'] == järjend[i::4]:
            xvaste += 1
        if ['O', 'O', 'O', 'X'] == järjend[i::4] or ['O', 'O', 'O', 'O'] == järjend[i::4] or ['X', 'O', 'O', 'O'] == järjend[i::4]:
            ovaste+=1
        elif ['X', 'X', 'X', 'O'] == järjend[i::4] or ['O', 'X', 'X', 'X'] == järjend[i::4] or ['X', 'X', 'X', 'X'] == järjend[i::4]:
            xvaste += 1
        i += 1
        
    if maatriks[0][0] == maatriks[1][1] == maatriks[2][2] == 'O':
        ovaste+=1
    if maatriks[1][1] == maatriks[2][2] == maatriks[3][3] == 'O':
        ovaste+=1
    if maatriks[3][0] == maatriks[1][2] == maatriks[2][1] == 'O':
        ovaste+=1
    if maatriks[0][3] == maatriks[1][2] == maatriks[2][1] == 'O':
        ovaste+=1
    if maatriks[3][3] == maatriks[1][1] == maatriks[2][2] == 'O':
        ovaste+=1
    if maatriks[3][2] == maatriks[1][0] == maatriks[2][1] == 'X':
        ovaste+=1
    if maatriks[0][0] == maatriks[1][1] == maatriks[2][2] == 'X':
        xvaste+=1
    if maatriks[1][1] == maatriks[2][2] == maatriks[3][3] == 'X':
        xvaste+=1
    if maatriks[3][3] == maatriks[1][1] == maatriks[2][2] == 'X':
        xvaste+=1
    if maatriks[3][2] == maatriks[1][0] == maatriks[2][1] == 'X':
        xvaste+=1
    if maatriks[3][0] == maatriks[1][2] == maatriks[2][1] == 'X':
        xvaste+=1
    if maatriks[0][3] == maatriks[1][2] == maatriks[2][1] == 'X':
        xvaste+=1
    
    
            
    vastus['O'] = ovaste
    vastus['X'] = xvaste
    return vastus
    

