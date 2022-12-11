def võitja(x):
    data={'O':0, 'X':0}
    X_count=0
    O_count=0
    for i in range(2):
        for j in range(2):
            u=(x[i][j]+x[i][j+1]+x[i][j+2])
            if u == "XXX":
                data['X']+=1
            if u == "OOO":
                data['O']+=1                
    for i in range(2):
        for j in range(2):
            u=(x[i][j]+x[i+1][j]+x[i+2][j])
            if u == "XXX":
                data['X']+=1
            if u == "OOO":
                data['O']+=1 
    for i in range(2):
        for j in range(2):
            u=(x[i][j]+x[i+1][j+1]+x[i+2][j+2])
            if u == "XXX":
                data['X']+=1
            if u == "OOO":
                data['O']+=1 
    for i in range(2):
        for j in range(2):
            u=(x[i][j+1]+x[i+1][j])
            if u == "XXX":
                data['X']+=1
            if u == "OOO":
                data['O']+=1  
    return data

