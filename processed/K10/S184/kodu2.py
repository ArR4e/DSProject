def võitja(maatriks):
    sõnastik={}
    X_loendur=0
    O_loendur=0
#read
    if maatriks[0][0]==maatriks[0][1]==maatriks[0][2]=="X":
        X_loendur+=1
    if maatriks[0][1]==maatriks[0][2]==maatriks[0][3]=="X":
        X_loendur+=1

    if maatriks[1][0]==maatriks[1][1]==maatriks[1][2]=="X":
        X_loendur+=1
    if maatriks[1][1]==maatriks[1][2]==maatriks[1][3]=="X":
        X_loendur+=1

    if maatriks[2][0]==maatriks[2][1]==maatriks[2][2]=="X":
        X_loendur+=1
    if maatriks[2][1]==maatriks[2][2]==maatriks[2][3]=="X":
        X_loendur+=1
        
    if maatriks[3][0]==maatriks[3][1]==maatriks[3][2]=="X":
        X_loendur+=1
    if maatriks[3][1]==maatriks[3][2]==maatriks[3][3]=="X":
        X_loendur+=1


    if maatriks[0][0]==maatriks[0][1]==maatriks[0][2]=="O":
        O_loendur+=1
    if maatriks[0][1]==maatriks[0][2]==maatriks[0][3]=="O":
        O_loendur+=1

    if maatriks[1][0]==maatriks[1][1]==maatriks[1][2]=="O":
        O_loendur+=1
    if maatriks[1][1]==maatriks[1][2]==maatriks[1][3]=="O":
        O_loendur+=1

    if maatriks[2][0]==maatriks[2][1]==maatriks[2][2]=="O":
        O_loendur+=1
    if maatriks[2][1]==maatriks[2][2]==maatriks[2][3]=="O":
        O_loendur+=1
        
    if maatriks[3][0]==maatriks[3][1]==maatriks[3][2]=="O":
        O_loendur+=1
    if maatriks[3][1]==maatriks[3][2]==maatriks[3][3]=="O":
        O_loendur+=1
#veerg
    if maatriks[0][0]==maatriks[1][0]==maatriks[2][0]=="X":
        X_loendur+=1
    if maatriks[1][0]==maatriks[2][0]==maatriks[3][0]=="X":
        X_loendur+=1
        
    if maatriks[0][1]==maatriks[1][1]==maatriks[2][1]=="X":
        X_loendur+=1
    if maatriks[1][1]==maatriks[2][1]==maatriks[3][1]=="X":
        X_loendur+=1
        
    if maatriks[0][2]==maatriks[1][2]==maatriks[2][2]=="X":
        X_loendur+=1
    if maatriks[1][2]==maatriks[2][2]==maatriks[3][2]=="X":
        X_loendur+=1
        
    if maatriks[0][3]==maatriks[1][3]==maatriks[2][3]=="X":
        X_loendur+=1
    if maatriks[1][3]==maatriks[2][3]==maatriks[3][3]=="X":
        X_loendur+=1


    if maatriks[0][0]==maatriks[1][0]==maatriks[2][0]=="O":
        O_loendur+=1
    if maatriks[1][0]==maatriks[2][0]==maatriks[3][0]=="O":
        O_loendur+=1
        
    if maatriks[0][1]==maatriks[1][1]==maatriks[2][1]=="O":
        O_loendur+=1
    if maatriks[1][1]==maatriks[2][1]==maatriks[3][1]=="O":
        O_loendur+=1
        
    if maatriks[0][2]==maatriks[1][2]==maatriks[2][2]=="O":
        O_loendur+=1
    if maatriks[1][2]==maatriks[2][2]==maatriks[3][2]=="O":
        O_loendur+=1
        
    if maatriks[0][3]==maatriks[1][3]==maatriks[2][3]=="O":
        O_loendur+=1
    if maatriks[1][3]==maatriks[2][3]==maatriks[3][3]=="O":
        O_loendur+=1

#diagonaal
    if maatriks[0][0]==maatriks[1][1]==maatriks[2][2]=="X":
        X_loendur+=1
    if maatriks[1][1]==maatriks[2][2]==maatriks[3][3]=="X":
        X_loendur+=1
        
    if maatriks[0][1]==maatriks[1][2]==maatriks[2][3]=="X":
        X_loendur+=1
    if maatriks[1][0]==maatriks[2][1]==maatriks[3][2]=="X":
        X_loendur+=1
        
    if maatriks[0][3]==maatriks[1][2]==maatriks[2][1]=="X":
        X_loendur+=1
    if maatriks[1][2]==maatriks[2][1]==maatriks[3][0]=="X":
        X_loendur+=1
        
    if maatriks[2][0]==maatriks[1][1]==maatriks[0][2]=="X":
        X_loendur+=1
    if maatriks[3][1]==maatriks[2][2]==maatriks[1][3]=="X":
        X_loendur+=1
        
        
    if maatriks[0][0]==maatriks[1][1]==maatriks[2][2]=="O":
        O_loendur+=1
    if maatriks[1][1]==maatriks[2][2]==maatriks[3][3]=="O":
        O_loendur+=1
        
    if maatriks[0][1]==maatriks[1][2]==maatriks[2][3]=="O":
        O_loendur+=1
    if maatriks[1][0]==maatriks[2][1]==maatriks[3][2]=="O":
        O_loendur+=1
        
    if maatriks[0][3]==maatriks[1][2]==maatriks[2][1]=="O":
        O_loendur+=1
    if maatriks[1][2]==maatriks[2][1]==maatriks[3][0]=="O":
        O_loendur+=1
        
    if maatriks[2][0]==maatriks[1][1]==maatriks[0][2]=="O":
        O_loendur+=1
    if maatriks[3][1]==maatriks[2][2]==maatriks[1][3]=="O":
        O_loendur+=1

    print("O: "+str(O_loendur))
    print("X: "+str(X_loendur))
    sõnastik["O"]=(O_loendur)
    sõnastik["X"]=(X_loendur)
    print(sõnastik)
    return sõnastik
võitja([['O',' ','O','X'],['O','O','X','X'],['O','X','O',' '],['X','X','X','O']])
