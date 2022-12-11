def võitja(maatriks):
    sümboldict = {}
    võidupunktid = {}
    for i in range(len(maatriks)):
        arvujärjend = maatriks[i]
        for j in range(len(arvujärjend)):
            sümbol = arvujärjend[j]
            sümboldict[(i, j)] = sümbol
    xvõit = 0
    ovõit = 0    
    iteratsioone = 16
    i = 0
    j = 0
    while iteratsioone > 0:
        sümbol1 = sümboldict.get((i, j))
        sümbol2p = sümboldict.get((i, j + 1))
        sümbol3p = sümboldict.get((i, j + 2))
        sümbol2d = sümboldict.get((i + 1, j + 1))
        sümbol3d = sümboldict.get((i + 2, j + 2))
        sümbol2dü = sümboldict.get((i - 1, j + 1))
        sümbol3dü = sümboldict.get((i - 2, j + 2))
        sümbol2a = sümboldict.get((i + 1, j))
        sümbol3a = sümboldict.get((i + 2, j))
        if sümbol1 == "X" and sümbol2p == "X" and sümbol3p == "X":
            xvõit += 1
        elif sümbol1 == "O" and sümbol2p == "O" and sümbol3p == "O":
            ovõit += 1
        
        if sümbol1 == "X" and sümbol2d == "X" and sümbol3d == "X":
            xvõit += 1
        elif sümbol1 == "O" and sümbol2d == "O" and sümbol3d == "O":
            ovõit += 1
        
        if sümbol1 == "X" and sümbol2dü == "X" and sümbol3dü == "X":
            xvõit += 1
        elif sümbol1 == "O" and sümbol2dü == "O" and sümbol3dü == "O":
            ovõit += 1
            
        if sümbol1 == "X" and sümbol2a == "X" and sümbol3a == "X":
            xvõit += 1
        elif sümbol1 == "O" and sümbol2a == "O" and sümbol3a == "O":
            ovõit += 1
        iteratsioone -= 1
        j += 1
        if j > 3:
            j = 0
            i += 1
    võidupunktid["O"] = ovõit
    võidupunktid["X"] = xvõit
    return võidupunktid