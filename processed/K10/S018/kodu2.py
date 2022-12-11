def võitja(laud):
    O = 0
    X = 0
    # reas
    for rida in laud:
        komb = ""
        for koht in rida:
            komb += koht
        if "XXXX" in komb:
            X += 2
        elif "XXX" in komb:
            X += 1
        if "OOOO" in komb:
            O += 2
        elif "OOO" in komb:
            O += 1
    # veerus
    for i in range(4):
        komb = ""
        for rida in laud:
            komb += rida[i]
        if "XXXX" in komb:
            X += 2
        elif "XXX" in komb:
            X += 1
        if "OOOO" in komb:
            O += 2
        elif "OOO" in komb:
            O += 1
    # diagonaalis v-p
    komb = laud[0][1] + laud[1][2] + laud[2][3]
    if "XXX" in komb:
        X += 1
    if "OOO" in komb:
        O += 1
    komb = laud[0][0] + laud[1][1] + laud[2][2] + laud[3][3]
    if "XXXX" in komb:
        X += 2
    elif "XXX" in komb:
        X += 1
    if "OOOO" in komb:
        O += 2
    elif "OOO" in komb:
        O += 1
    komb = laud[1][0] + laud[2][1] + laud[3][2]
    if "XXX" in komb: 
        X += 1
    if "OOO" in komb:
        O += 1
    # diagonaalis p-v
    komb = laud[0][2] + laud[1][1] + laud[2][0]
    if "XXX" in komb:
        X += 1
    if "OOO" in komb:
        O += 1
    komb = laud[0][3] + laud[1][2] + laud[2][1] + laud[3][0]
    if "XXXX" in komb:
        X += 2
    elif "XXX" in komb:
        X += 1
    if "OOOO" in komb:
        O += 2
    elif "OOO" in komb:
        O += 1
    komb = laud[1][3] + laud[2][2] + laud[3][1]
    if "XXX" in komb: 
        X += 1
    if "OOO" in komb:
        O += 1
        
    tulemus = {}
    tulemus["O"] = O
    tulemus["X"] = X
                
    return tulemus