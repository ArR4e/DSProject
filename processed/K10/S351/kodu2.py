def võitja(maatriks):
    vastus={}
    #O esinemine reas
    read=0
    O_arv=0
    while read<=3:
        #for read in maatriks:
        if (maatriks[read][1])=="O" and (maatriks[read][2])=="O" and (maatriks[read][3])=="O" and (maatriks[read][0])=="O":
            vastus["O"]=O_arv+2
            read+=1
        elif (maatriks[read][0])=="O" and (maatriks[read][1])=="O" and (maatriks[read][2])=="O" and (maatriks[read][3])!="O":
            vastus["O"]=O_arv+1
            read+=1
        elif (maatriks[read][1])=="O" and (maatriks[read][2])=="O" and (maatriks[read][3])=="O" and (maatriks[read][0])!="O":
            vastus["O"]=O_arv+1
            read+=1
        else:
            vastus["O"]=O_arv
            read+=1
            
    #X esinemine reas
    read=0
    X_arv=0
    while read<=3:
        #for read in maatriks:
        if (maatriks[read][1])=="X" and (maatriks[read][2])=="X" and (maatriks[read][3])=="X" and (maatriks[read][0])=="X":
            vastus["X"]=X_arv+2
            read+=1
        elif (maatriks[read][0])=="X" and (maatriks[read][1])=="X" and (maatriks[read][2])=="X" and (maatriks[read][3])!="X":
            vastus["X"]=X_arv+1
            read+=1
        elif (maatriks[read][1])=="X" and (maatriks[read][2])=="X" and (maatriks[read][3])=="X" and (maatriks[read][0])!="X":
            vastus["X"]=X_arv+1
            read+=1
        
        else:
            vastus["X"]=X_arv
            read+=1
    #O esinemine tulbas
    tulp=0
    while tulp<=3:
        #for tulp in maatriks:
        if (maatriks[0][tulp])=="O" and (maatriks[1][tulp])=="O" and (maatriks[2][tulp])=="O" and (maatriks[3][tulp])=="O":
            vastus["O"]=O_arv+2
            tulp+=1
        elif (maatriks[0][tulp])=="O" and (maatriks[1][tulp])=="O" and (maatriks[2][tulp])=="O" and (maatriks[3][tulp])!="O":
            vastus["O"]=O_arv+1
            tulp+=1
        elif (maatriks[0][tulp])=="O" and (maatriks[1][tulp])=="O" and (maatriks[2][tulp])=="O" and (maatriks[3][tulp])!="O":
            vastus["O"]=O_arv+1
            tulp+=1
        else:
            vastus["O"]=O_arv
            tulp+=1
    
    #X esinemine tulbas
    tulp=0
    while tulp<=3:
        #for tulp in maatriks:
        if (maatriks[0][tulp])=="X" and (maatriks[1][tulp])=="X" and (maatriks[2][tulp])=="X" and (maatriks[3][tulp])=="X":
            vastus["X"]=X_arv+2
            tulp+=1
        elif (maatriks[0][tulp])=="X" and (maatriks[1][tulp])=="X" and (maatriks[2][tulp])=="X" and (maatriks[3][tulp])!="X":
            vastus["X"]=X_arv+1
            tulp+=1
        elif (maatriks[0][tulp])=="X" and (maatriks[1][tulp])=="X" and (maatriks[2][tulp])=="X" and (maatriks[3][tulp])!="X":
            vastus["X"]=X_arv+1
            tulp+=1
        else:
            vastus["X"]=X_arv
            tulp+=1
            
    #O ESINEMINE DIAGONAALIS
    #4-diagonaalid vasakult paremale
    if maatriks[0][0]=="O" and maatriks[1][1]=="O" and maatriks[2][2]=="O" and maatriks[3][3]=="O":
        vastus["O"]=O_arv+2
    elif maatriks[0][0]=="O" and maatriks[1][1]=="O" and maatriks[2][2]=="O" and maatriks[3][3]!="O":
        vastus["O"]=O_arv+1
    elif maatriks[0][0]!="O" and maatriks[1][1]=="O" and maatriks[2][2]=="O" and maatriks[3][3]=="O":
        vastus["O"]=O_arv+1
    #4-diagonaalid paremalt vasakule
    if maatriks[0][3]=="O" and maatriks[1][2]=="O" and maatriks[2][1]=="O" and maatriks[3][0]=="O":
        vastus["O"]=O_arv+2
    elif maatriks[0][3]=="O" and maatriks[1][2]=="O" and maatriks[2][1]=="O" and maatriks[3][0]!="O":
        vastus["O"]=O_arv+1
    elif maatriks[0][3]!="O" and maatriks[1][2]=="O" and maatriks[2][1]=="O" and maatriks[3][0]=="O":
        vastus["O"]=O_arv+1
    #3-diagonaalid 
    if maatriks[2][0]=="O" and maatriks[1][1]=="O" and maatriks[0][3]=="O":
        vastus["O"]=O_arv+1
    if maatriks[3][1]=="O" and maatriks[2][2]=="O" and maatriks[1][3]=="O":
        vastus["O"]=O_arv+1
    if maatriks[1][0]=="O" and maatriks[2][1]=="O" and maatriks[3][2]=="O":
        vastus["O"]=O_arv+1
    if maatriks[0][1]=="O" and maatriks[1][2]=="O" and maatriks[2][3]=="O":
        vastus["O"]=O_arv+1
        
    #X ESINEMINE DIAGONAALIS
    #4-diagonaalid vasakult paremale
    if maatriks[0][0]=="X" and maatriks[1][1]=="X" and maatriks[2][2]=="X" and maatriks[3][3]=="X":
        vastus["X"]=X_arv+2
    if maatriks[0][0]=="X" and maatriks[1][1]=="X" and maatriks[2][2]=="X" and maatriks[3][3]!="X":
        vastus["X"]=X_arv+1
    if maatriks[0][0]!="X" and maatriks[1][1]=="X" and maatriks[2][2]=="X" and maatriks[3][3]=="X":
        vastus["X"]=X_arv+1        
    #4-diagonaalid paremalt vasakule
    if maatriks[0][3]=="X" and maatriks[1][2]=="X" and maatriks[2][1]=="X" and maatriks[3][0]=="X":
        vastus["X"]=X_arv+2
    if maatriks[0][3]=="X" and maatriks[1][2]=="X" and maatriks[2][1]=="X" and maatriks[3][0]!="X":
        vastus["X"]=X_arv+1
    if maatriks[0][3]!="X" and maatriks[1][2]=="X" and maatriks[2][1]=="X" and maatriks[3][0]=="X":
        vastus["X"]=X_arv+1
        
    #3-diagonaalid
    if maatriks[2][0]=="X" and maatriks[1][1]=="X" and maatriks[0][3]=="X":
        vastus["X"]=X_arv+1
    if maatriks[3][1]=="X" and maatriks[2][2]=="X" and maatriks[1][3]=="X":
        vastus["X"]=X_arv+1
    if maatriks[1][0]=="X" and maatriks[2][1]=="X" and maatriks[3][2]=="X":
        vastus["X"]=X_arv+1
    if maatriks[0][1]=="X" and maatriks[1][2]=="X" and maatriks[2][3]=="X":
        vastus["X"]=X_arv+1
        
        
    return vastus
    
võitja([['X','X','X',' '],
            [' ','O',' ',' '],
            [' ',' ','O',' '],
            [' ',' ',' ','O']])
    
