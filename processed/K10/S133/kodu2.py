import copy
def võitja(maatriks):
    O=0
    X=0
    maatriks2=copy.deepcopy(maatriks)
    for i in range(len(maatriks)):
        for j in range(len(maatriks)):
            if maatriks[i][j]=="O":
                maatriks[i][j]=1
                maatriks2[i][j]=0
            elif maatriks[i][j]=="X":
                maatriks2[i][j]=1
                maatriks[i][j]=0
            elif maatriks[i][j]==" ":
                maatriks2[i][j]=0
                maatriks[i][j]=0
            elif maatriks[i][j]=="":
                maatriks[i][j]=0
                maatriks2[i][j]=0

    for n in range(len(maatriks)):
        #read 
        if int(maatriks[n][0])+int(maatriks[n][1])+int(maatriks[n][2])+int(maatriks[n][3])>3:
            O+=2
        elif int(maatriks[n][0])+int(maatriks[n][1])+int(maatriks[n][2])+int(maatriks[n][3])==3:
            O+=1
            
        if int(maatriks2[n][0])+int(maatriks2[n][1])+int(maatriks2[n][2])+int(maatriks2[n][3])>3:
            X+=2
        elif int(maatriks2[n][0])+int(maatriks2[n][1])+int(maatriks2[n][2])+int(maatriks2[n][3])==3:
            X+=1
            
        #veerud
        if int(maatriks[0][n])+int(maatriks[1][n])+int(maatriks[2][n])+int(maatriks[3][n])>3:
            O+=2
        elif int(maatriks[0][n])+int(maatriks[1][n])+int(maatriks[2][n])+int(maatriks[3][n])==3:
            O+=1
        if int(maatriks2[0][n])+int(maatriks2[1][n])+int(maatriks2[2][n])+int(maatriks2[3][n])>3:
            X+=2
        elif int(maatriks2[0][n])+int(maatriks2[1][n])+int(maatriks2[2][n])+int(maatriks2[3][n])==3:
            X+=1  

#muu/horisontaalid
    if int(maatriks[0][0])+int(maatriks[1][1])+int(maatriks[2][2])+int(maatriks[3][3])>3:
        O+=2
    elif int(maatriks[0][0])+int(maatriks[1][1])+int(maatriks[2][2])+int(maatriks[3][3])==3:
        O+=1
        
    if int(maatriks[0][1])+int(maatriks[1][2])+int(maatriks[2][3])>3:
        O+=2
    elif int(maatriks[0][1])+int(maatriks[1][2])+int(maatriks[2][3])==3:
        O+=1

    if int(maatriks[1][0])+int(maatriks[2][1])+int(maatriks[3][2])>3:
        O+=2
    elif int(maatriks[1][0])+int(maatriks[2][1])+int(maatriks[3][2])==3:
        O+=1            
            
    if int(maatriks2[0][0])+int(maatriks2[1][1])+int(maatriks2[2][2])+int(maatriks2[3][3])>3:
        X+=2
    elif int(maatriks2[0][0])+int(maatriks2[1][1])+int(maatriks2[2][2])+int(maatriks2[3][3])==3:
        X+=1
            
    if int(maatriks2[0][1])+int(maatriks2[1][2])+int(maatriks2[2][3])>3:
        X+=2
    elif int(maatriks2[0][1])+int(maatriks2[1][2])+int(maatriks2[2][3])==3:
        X+=1
            
    if int(maatriks2[1][0])+int(maatriks2[2][1])+int(maatriks2[3][2])>3:
        X+=2
    elif int(maatriks2[1][0])+int(maatriks2[2][1])+int(maatriks2[3][2])==3:
        X+=1

#vasakult ülevalt paremale alla
    if int(maatriks[3][0])+int(maatriks[2][1])+int(maatriks[1][2])+int(maatriks[0][3])>3:
        O+=2
    elif int(maatriks[3][0])+int(maatriks[2][1])+int(maatriks[1][2])+int(maatriks[0][3])==3:
        O+=1
        
    if int(maatriks[1][3])+int(maatriks[2][2])+int(maatriks[3][1])>3:
        O+=2
    elif int(maatriks[1][3])+int(maatriks[2][2])+int(maatriks[3][1])==3:
        O+=1

    if int(maatriks[2][0])+int(maatriks[1][1])+int(maatriks[0][2])>3:
        O+=2
    elif int(maatriks[2][0])+int(maatriks[1][1])+int(maatriks[0][2])==3:
        O+=1            
            
    if int(maatriks2[3][0])+int(maatriks2[2][1])+int(maatriks2[1][2])+int(maatriks2[0][3])>3:
        X+=2
    elif int(maatriks2[3][0])+int(maatriks2[2][1])+int(maatriks2[1][2])+int(maatriks2[0][3])==3:
        X+=1

    if int(maatriks2[1][3])+int(maatriks2[2][2])+int(maatriks2[3][1])>3:
        X+=2
    elif int(maatriks2[1][3])+int(maatriks2[2][2])+int(maatriks2[3][1])==3:
        X+=1

    if int(maatriks2[2][0])+int(maatriks2[1][1])+int(maatriks2[0][2])>3:
        X+=2
    elif int(maatriks2[2][0])+int(maatriks2[1][1])+int(maatriks2[0][2])==3:
        X+=1


    vastus={}
    vastus["O"]=O
    vastus["X"]=X
    return vastus
print(võitja([['O',' ',' ','X'],
            [' ','O','X',' '],
            [' ','X','O',' '],
            ['X',' ',' ','O']]))