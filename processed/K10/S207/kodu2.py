def võitja(maatriks):
    Xvõit = 0
    Ovõit = 0
    
    #kontrollib neljas miinoris diagonaalid üle
    v = [[[0,3],[0,3]],[[1,4],[0,3]],[[0,3],[1,4]],[[1,4],[1,4]]]
    for x in range(0,4):
        alamaatriks = maatriks[v[x][0][0]:v[x][0][1]]
        for i in range(0,3):
            alamaatriks[i] = alamaatriks[i][v[x][1][0]:v[x][1][1]]
        if alamaatriks[0][0]=="X" and alamaatriks[1][1]=="X" and alamaatriks[2][2]=="X":
            Xvõit +=1
        if alamaatriks[0][0]=="O" and alamaatriks[1][1]=="O" and alamaatriks[2][2]=="O":
            Ovõit += 1
        if alamaatriks[0][2]=="X" and alamaatriks[1][1]=="X" and alamaatriks[2][0]=="X":
            Xvõit +=1
        if alamaatriks[0][2]=="O" and alamaatriks[1][1]=="O" and alamaatriks[2][0]=="O":
            Ovõit += 1
            
    #kontrollib iga rea üle, siis vahetab veerud ja read ning teeb uuesti        
    for i in range(0,2):
        for rida in maatriks:
            if rida[0:3].count("X") == 3:
                Xvõit += 1
            if rida[0:3].count("O") == 3:
                Ovõit += 1
            if rida[1:4].count("X") == 3:
                Xvõit += 1
            if rida[1:4].count("O") == 3:
                Ovõit += 1
        maatriks = list(zip(maatriks[0],maatriks[1],maatriks[2],maatriks[3],))
    nimekiri = {}
    nimekiri["O"] = Ovõit
    nimekiri["X"] = Xvõit
    return nimekiri
#see on väga väga väga halb kood ja ma tean seda, aga ma ei viitsid seda uuesti kirjutada