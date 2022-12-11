def võitja(seis):
    x = 0
    o = 0
    kord = {}
    kord["O"] = o
    kord["X"] = x
    for i in range(len(seis[0])):
        for j in range(len(seis[i])):
            if seis[i][j] == "X":
                x += 1
            elif seis[i][j] == "O":
                o += 1
            else:
                continue
    print(kord)
    
võitja([['X','X','X',' '],
            [' ','O',' ',' '],
            [' ',' ','O',' '],
            [' ',' ',' ','O']])
        
