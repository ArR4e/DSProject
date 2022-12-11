#trips traps trull


#m = [["O",'O','O','O'], ['X','X','X','X'], ['X','X','X','X'], ['X','X','X','X']]
def võitja(m):
    võitjaX = 0
    võitjaO = 0

    #diagonaal1
    sõne1 = ""
    for i in range(0,4):
        a = m[i][i]
        sõne1 += a
        
        arv1 = sõne1.count("X")
        arv2 = sõne1.count("O")
        
    if arv1 >= 3:
        võitjaX += 1
    if arv2 >= 3:
        võitjaO += 1
    if arv1 >= 4:
        võitjaX += 1
    if arv2 >= 4:
        võitjaO += 1    
    #diagonaalid2
    sõne2 = ""
    i3 = 0
    for i in range(3, -1, -1):
        a = m[i][i3]
        sõne2 += a
        
        arv1 = sõne2.count("X")
        arv2 = sõne2.count("O")
#        print(arv1)
#        print(arv2)
        i3 += 1
    if arv1 >= 3:
        võitjaX += 1 
    if arv2 >= 3:
        võitjaO += 1
    if arv1 >= 4:
        võitjaX += 1 
    if arv2 >= 4:
        võitjaO += 1
        
        
    #diagonaalid1_2
    i4 = 0
    sõne3 = ""
    sõne4 = ""
    while i4<3:
        a = m[i4][i4+1]
        b = m[i4+1][i4]
#        print(b)
        sõne3 += a
        sõne4 += b

        arv1 = sõne3.count("X")
        arv2 = sõne3.count("O")        
        arv3 = sõne4.count("X")
        arv4 = sõne4.count("O")
#        print(arv1)
#        print(arv2)
#        print(arv3)
#        print(arv4)
        
        
        if arv1 >= 3:
            võitjaX += 1 
        if arv2 >= 3:
            võitjaO += 1
        if arv3 >= 3:
            võitjaX += 1 
        if arv4 >= 3:
            võitjaO += 1
        i4 += 1

    #diagonaalid2_2
    i5 = 0
    i6 = 0
    sõne5 = ""
    sõne6 = ""
    while i5<3:
        a = m[i5][i6+2]
        b = m[i5+1][i6+3]
        
        sõne5 += a
        sõne6 += b

        arv1 = sõne5.count("X")
        arv2 = sõne5.count("O")
        arv3 = sõne6.count("X")
        arv4 = sõne6.count("O")
#        print(arv1)
#        print(arv2)
#        print(arv3)
#        print(arv4)
        
        if arv1 >= 3:
            võitjaX += 1 
        if arv2 >= 3:
            võitjaO += 1
        if arv3 >= 3:
            võitjaX += 1 
        if arv4 >= 3:
            võitjaO += 1

        
        i5 += 1
        i6 -= 1

#------
#rea-veeru tsükklis on probleem, kus 3 korda jääb mõnikord lugemata või muudatusel ei lisandu juurde. võimalik, et tasub eraldada read ja veerud
    #read
    i1=0
    while i1<4:
        sõne = ""
        for i in range(0, 4):
            a = m[i1][i]
            sõne += a
        arv1 = sõne.count("X")
        arv2 = sõne.count("O")
#        print(arv1)
#        print(arv2)
        
        if arv1 >= 3:
            võitjaX += 1 
        if arv2 >= 3:
            võitjaO += 1
        if arv1 >= 4:
            võitjaX += 1 
        if arv2 >= 4:
            võitjaO += 1
        
        
        i1 += 1
    
    #veerud
    i2=0
    while i2<4:
        sõne = ""
        for i in range(0, 4):
            a = m[i][i2]
            sõne += a
            arv1 = sõne.count("X")
            arv2 = sõne.count("O")
#        print(arv1)
#        print(arv2)
        if arv1 >= 3:
            võitjaX += 1 
        if arv2 >= 3:
            võitjaO += 1
        if arv1 >= 4:
            võitjaX += 1 
        if arv2 >= 4:
            võitjaO += 1
        
        i2 += 1

    sõnastik = {}
    sõnastik["O"] = võitjaO
    sõnastik["X"] = võitjaX
    return sõnastik
#print(võitja(m))