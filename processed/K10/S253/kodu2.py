def võitja(m):
    x_e = 0
    o_e = 0

    #
    for i in range(4):
        if (m[i][0] == "X" or m[i][0] == "O") and m[i][1] == m[i][0] and m[i][2] == m[i][0]:
            if m[i][0] == "X":
                x_e += 1
            else:
                o_e += 1
        if (m[i][1] == "X" or m[i][1] == "O") and m[i][2] == m[i][1] and m[i][3] == m[i][1]:
            if m[i][1] == "X":
                x_e += 1
            else:
                o_e += 1
    #
    for i in range(4):
        if (m[0][i] == "X" or m[0][i] == "O") and m[1][i] == m[0][i] and m[2][i] == m[0][i]:
            if m[0][i] == "X":
                x_e += 1
            else:
                o_e += 1
        if (m[1][i] == "X" or m[1][i] == "O") and m[2][i] == m[1][i] and m[3][i] == m[1][i]:
            if m[1][i] == "X":
                x_e += 1
            else:
                o_e += 1
                
    #
    for i in range(2):
        if (m[0][i] == "X" or m[0][i] == "O") and m[1][i+1] == m[0][i] and m[2][i+2] == m[0][i]:
            if m[0][i] == "X":
                x_e += 1
            else:
                o_e += 1
        if (m[1][i] == "X" or m[1][i] == "O") and m[2][i+1] == m[1][i] and m[3][i+2] == m[1][i]:
            if m[1][i] == "X":
                x_e += 1
            else:
                o_e += 1
    #            
    for i in range(2):
        if (m[0][i+2] == "X" or m[0][i+2] == "O") and m[1][i+1] == m[0][i+2] and m[2][i] == m[0][i+2]:
            if m[0][i+2] == "X":
                x_e += 1
            else:
                o_e += 1
        if (m[1][i+2] == "X" or m[1][i+2] == "O") and m[2][i+1] == m[1][i+2] and m[3][i] == m[1][i+2]:
            if m[1][i+2] == "X":
                x_e += 1
            else:
                o_e += 1                   
                
    return {'O':o_e, 'X':x_e}
    ## #######################       
                   
            

            
            
            
            