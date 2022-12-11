def võitja(m):
    X=0
    O=0
    skoor={'X':0,'O':0}
    rida=0
    
    for i in m:
        nr=0
        for j in i:
            if j!='X' and j!='O':
                nr+=1
                continue
            if nr<2:
                if j==m[rida][nr+1]==m[rida][nr+2]:#read
                    if j=='X':
                        X+=1
                        skoor['X']=X
                    elif j=='O':
                        O+=1
                        skoor['O']=O
            if rida>1:
                nr+=1
                continue
            if nr<2:
                if j==m[rida+1][nr+1]==m[rida+2][nr+2]:#diagonaal
                    if j=='X':
                        X+=1
                        skoor['X']=X
                    elif j=='O':
                        O+=1
                        skoor['O']=O
                       
            if j==m[rida+1][nr]==m[rida+2][nr]:#veerud
                if j=='X':
                    X+=1
                    skoor['X']=X
                elif j=='O':
                    O+=1
                    skoor['O']=O                     
                
            if nr>1:
                if j==m[rida+1][nr-1]==m[rida+2][nr-2]:#tagurpidi diagonaal
                    if j=='X':
                        X+=1
                        skoor['X']=X
                    elif j=='O':
                        O+=1
                        skoor['O']=O
            nr+=1
        rida+=1
            
    return skoor