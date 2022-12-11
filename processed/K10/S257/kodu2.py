def võitja(a : list):
    voit = {"O": 0, "X": 0}
    i = 0
    while i <= 3:
        mark = ""
        if a[i][1] == "X" and a[i][2] == "X":
            mark = "X"
        elif a[i][1] == "O" and a[i][2] == "O":
            mark = "O"
        if a[i][3] == mark:
            voit[mark] += 1
        if a[i][0] == mark:
            voit[mark] += 1
        i += 3
    
    i = 0
    while i <= 3:
        mark = ""
        if a[1][i] == "X" and a[2][i] == "X":
            mark = "X"
        elif a[1][i] == "O" and a[2][i] == "O":
            mark = "O"
        if a[3][i] == mark:
            voit[mark] += 1
        if a[0][i] == mark:
            voit[mark] += 1
        i += 3
    i = 1
    while i <= 2:
        j = 1
        while j <= 2:
            mark = ""
            if a[i][j] == "O":
                mark = "O"
            elif a[i][j] == "X":
                mark = "X"
            if (a[i-1][j-1] == mark and a[i+1][j+1] == mark):
                voit[mark] += 1
            if (a[i-1][j+1] == mark and a[i+1][j-1] == mark):
                voit[mark] += 1
            if (a[i+1][j] == mark and a[i-1][j] == mark):
                voit[mark] += 1
            if (a[i][j+1] == mark and a[i][j-1] == mark):
                voit[mark] += 1
            j += 1
        i += 1
    return voit

    
                
            
        