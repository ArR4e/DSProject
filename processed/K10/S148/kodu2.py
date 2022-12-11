def võitja(a):
    h = {"O" : 0,
         "X" : 0,}
    
    # read
    
    for rida in a:
        v = ""
        for el in rida:
            if el == "O":
                v += "O"
            elif el == "X":
                v += "X"
            else:
                v += " "
            
        if "OOOO" in v:
            h["O"] = h.get("O", 0) + 2
        elif "OOO" in v:
            h["O"] = h.get("O", 0) + 1
        elif "XXXX" in v:
            h["X"] = h.get("X", 0) + 2
        elif "XXX" in v:
            h["X"] = h.get("X", 0) + 1
    
    # veerud
    
    i = 0
    while i < 4:
        if a[0][i] == a[1][i] == a[2][i] == a[3][i]:
            h[a[0][i]] = h.get(a[0][i], 0) + 2
        elif a[0][i] == a[1][i] == a[2][i] or a[1][i] == a[2][i] == a[3][i]:
            h[a[1][i]] = h.get(a[1][i], 0) + 1
        
        i += 1
    
    # diagonaalid
    
    if a[0][0] == a[1][1] == a[2][2] == a[3][3]:
        h[a[0][0]] = h.get(a[0][0], 0) + 2
    elif a[0][0] == a[1][1] == a[2][2] or a[1][1] == a[2][2] == a[3][3]:
        h[a[1][1]] = h.get(a[1][1], 0) + 1
    if a[0][3] == a[1][2] == a[2][1] == a[3][0]:
        h[a[0][3]] = h.get(a[0][3], 0) + 2
    elif a[0][3] == a[1][2] == a[2][1] or a[1][2] == a[2][1] == a[3][0]:
        h[a[1][2]] = h.get(a[1][2], 0) + 1
    if a[0][1] == a[1][2] == a[2][3]:
        h[a[0][1]] = h.get(a[0][1], 0) + 1
    if a[1][0] == a[2][1] == a[3][2]:
        h[a[1][0]] = h.get(a[1][0], 0) + 1
    if a[0][2] == a[1][1] == a[2][0]:
        h[a[0][2]] = h.get(a[0][2], 0) + 1
    if a[1][3] == a[2][2] == a[3][1]:
        h[a[1][3]] = h.get(a[1][3], 0) + 1
    
    if " " in h:
        del h[" "]
    
    return h