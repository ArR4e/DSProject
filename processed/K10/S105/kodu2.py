def võitja(a):
    ocount=0
    xcount=0
    b=[]
    c=[]
    d=[]
    f=[]
    flip=[b,c,d,f]
    for j in a:
        if (j[1]=="X" and j[2]=="X"):
            if j[0]=="X":
                xcount+=1
            if j[3]=="X":
                xcount+=1
        if (j[1]=="O" and j[2]=="O"): 
            if j[0]=="O":
                ocount+=1
            if j[3]=="O":
                ocount+=1
        b.append(j[0])
        c.append(j[1])
        d.append(j[2])
        f.append(j[3])
    for ele in flip:
        if (ele[1]=="X" and ele[2]=="X"):
            if ele[0]=="X":
                xcount+=1
            if ele[3]=="X":
                xcount+=1
        if (ele[1]=="O" and ele[2]=="O"): 
            if ele[0]=="O":
                ocount+=1
            if ele[3]=="O":
                ocount+=1
    j1=a[0]
    j2=a[1]
    j3=a[2]
    j4=a[3]
    
    if j2[0]=="X" and j3[1]=="X" and j4[2]=="X":
        xcount+=1
    if j1[0]=="X" and j2[1]=="X" and j3[2]=="X":
        xcount+=1
    if j2[1]=="X" and j3[2]=="X" and j4[3]=="X":
        xcount+=1
    if j1[1]=="X" and j2[2]=="X" and j3[3]=="X":
        xcount+=1
    if j1[2]=="X" and j2[1]=="X" and j3[0]=="X":
        xcount+=1
    if j1[3]=="X" and j2[2]=="X" and j3[1]=="X":
        xcount+=1
    if j2[2]=="X" and j3[1]=="X" and j4[0]=="X":
        xcount+=1
    if j2[3]=="X" and j3[2]=="X" and j4[1]=="X":
        xcount+=1
    if j2[0]=="O" and j3[1]=="O" and j4[2]=="O":
        ocount+=1
    if j1[0]=="O" and j2[1]=="O" and j3[2]=="O":
        ocount+=1
    if j2[1]=="O" and j3[2]=="O" and j4[3]=="O":
        ocount+=1
    if j1[1]=="O" and j2[2]=="O" and j3[3]=="O":
        ocount+=1
    if j1[2]=="O" and j2[1]=="O" and j3[0]=="O":
        ocount+=1
    if j1[3]=="O" and j2[2]=="O" and j3[1]=="O":
        ocount+=1
    if j2[2]=="O" and j3[1]=="O" and j4[0]=="O":
        ocount+=1
    if j2[3]=="O" and j3[2]=="O" and j4[1]=="O":
        ocount+=1
        
    return {"O":ocount, "X":xcount}
võitja ([[' ', 'O', 'X', ' '], ['O', 'X', 'O', 'X'], ['X', 'O', 'X', 'O'], [' ', 'X', 'O', ' ']])