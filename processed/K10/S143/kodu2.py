def võitja(m):
    v = {"O":0,"X":0}
    tm = list(map(list,zip(*m)))
    for i in range(8):
        y = i // 2
        x = i % 2
        if set(m[y][x:x+3])=={"O"}:
            v["O"]+=1
        elif set(m[y][x:x+3])=={"X"}:
            v["X"]+=1
        if set(tm[y][x:x+3])=={"O"}:
            v["O"]+=1
        elif set(tm[y][x:x+3])=={"X"}:
            v["X"]+=1
    for j in range(2):
        if [m[i][i] for i in range(j,j+3)].count("O")==3:
            v["O"]+=1
        elif [m[i][i] for i in range(j,j+3)].count("X")==3:
            v["X"]+=1
        if [m[i][-i-1] for i in range(j,j+3)].count("O")==3:
            v["O"]+=1
        elif [m[i][-i-1] for i in range(j,j+3)].count("X")==3:
            v["X"]+=1
    if [m[i][i+1] for i in range(3)].count("O")==3:
        v["O"]+=1
    elif [m[i][i+1] for i in range(3)].count("X")==3:
        v["X"]+=1
    if [m[i+1][i] for i in range(3)].count("O")==3:
        v["O"]+=1
    elif [m[i+1][i] for i in range(3)].count("X")==3:
        v["X"]+=1
    if [m[i][2-i] for i in range(3)].count("O")==3:
        v["O"]+=1
    elif [m[i][2-i] for i in range(3)].count("X")==3:
        v["X"]+=1
    if [m[i+1][3-i] for i in range(3)].count("O")==3:
        v["O"]+=1
    elif [m[i+1][3-i] for i in range(3)].count("X")==3:
        v["X"]+=1
        
        
    
    
    
    return v  
      
print(võitja([['O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O']]))
