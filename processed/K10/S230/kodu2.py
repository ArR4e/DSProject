def võitja(a):
    X_arv=0
    O_arv=0
    #Horisontaalselt
    for i in range(4):
        for j in range(2):
            u=a[i][j]+a[i][j+1]+a[i][j+2]
            if u == "XXX":
                X_arv+=1
            if u == "OOO":
                O_arv+=1
    #Vertikaalselt
    for i in range(2):
        for j in range(4):
            u=a[i][j]+a[i+1][j]+a[i+2][j]
            if u == "XXX":
                X_arv+=1
            if u == "OOO":
                O_arv+=1
    #Diagonaalselt alla
    for i in range(2):
        for j in range(2):
            u=a[i][j]+a[i+1][j+1]+a[i+2][j+2]
            if u == "XXX":
                X_arv+=1
            if u == "OOO":
                O_arv+=1
    #Diagonaalselt üles
    for i in range(2,4):
        for j in range(2):
            u=a[i][j]+a[i-1][j+1]+a[i-2][j+2]
            if u == "XXX":
                X_arv+=1
            if u == "OOO":
                O_arv+=1
    s={"O":O_arv,"X":X_arv}
    return s