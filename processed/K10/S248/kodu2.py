def võitja(x):
    s={"O":0, "X":0}
    for i in range(4):
        if "X"==x[i][0]==x[i][1]==x[i][2]:
            s["X"]+=1
            if "X"==x[i][1]==x[i][2]==x[i][3]:
                s["X"]+=1
        elif "X"==x[i][1]==x[i][2]==x[i][3]:
            s["X"]+=1
        elif "O"==x[i][0]==x[i][1]==x[i][2]:
            s["O"]+=1
            if "O"==x[i][1]==x[i][2]==x[i][3]:
                s["O"]+=1
        elif "O"==x[i][1]==x[i][2]==x[i][3]:
            s["O"]+=1
    
    for i in range(4):
        if "X"==x[0][i]==x[1][i]==x[2][i]:
            s["X"]+=1
            if "X"==x[1][i]==x[2][i]==x[3][i]:
                s["X"]+=1
        elif "X"==x[1][i]==x[2][i]==x[3][i]:
            s["X"]+=1
        elif "O"==x[0][i]==x[1][i]==x[2][i]:
            s["O"]+=1
            if "O"==x[1][i]==x[2][i]==x[3][i]:
                s["O"]+=1
        elif "O"==x[1][i]==x[2][i]==x[3][i]:
            print (x[1][i])
            s["O"]+=1
    
    for i in range(2):
        for j in range(2):
            if "X"==x[i][j]==x[i+1][j+1]==x[i+2][j+2]:
                s["X"]+=1
                
    for i in range(2):
        for j in range(2):
            if "O"==x[i][j]==x[i+1][j+1]==x[i+2][j+2]:
                s["O"]+=1
                
    for i in range(2):
        for j in range(2):
            if "X"==x[i+2][j+0]==x[i+1][j+1]==x[i][j+2]:
                s["X"]+=1
                
    for i in range(2):
        for j in range(2):
            if "O"==x[i+2][j+0]==x[i+1][j+1]==x[i][j+2]:
                s["O"]+=1
                
    return s



            
        

        

    