def võitja(m):
    x = 0
    o = 0
    
    for i in range(0,2):
        for n in range(0,4):
            a = m[i][n] + m[i+1][n] + m[i+2][n]
            if a == "XXX":
                x += 1
            elif a == "OOO":
                o += 1
                
    for i in range(0,2):
        for n in range(0,4):
            a = m[n][i] + m[n][i+1] + m[n][i+2]
            if a == "XXX":
                x += 1
            elif a == "OOO":
                o += 1
                
    for i in range(0,2):
        for n in range(0,2):
            a = m[n][i] + m[n+1][i+1] + m[n+2][i+2]
            if a == "XXX":
                x += 1
            elif a == "OOO":
                o += 1
            
    for i in range(0,2):
        for n in range(3,1,-1):
            a = m[n][i] + m[n-1][i+1] + m[n-2][i+2]
            if a == "XXX":
                x += 1
            elif a == "OOO":
                o += 1
    return {"O":o, "X":x}