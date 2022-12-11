def võitja(maatriks):
    X_loendur=0
    O_loendur=0
    tulemus={}
    tulemus['X']=0
    tulemus['O']=0
    
    for i in range(4):
        X_loendur=0
        O_loendur=0
        for j in range(4):
            if maatriks[i][j]=='X':
                X_loendur+=1
                O_loendur=0
            elif maatriks[i][j]=='O':
                O_loendur+=1
                X_loendur=0
            else:
                X_loendur=0
                O_loendur=0
            if X_loendur>=3:
                tulemus['X']+=1
            if O_loendur>=3:
                tulemus['O']+=1
                
                
    for i in range(4):
        X_loendur=0
        O_loendur=0
        for j in range(4):
            if maatriks[j][i]=='X':
                X_loendur+=1
                O_loendur=0
            elif maatriks[j][i]=='O':
                O_loendur+=1
                X_loendur=0
            else:
                X_loendur=0
                O_loendur=0
            if X_loendur>=3:
                tulemus['X']+=1
            if O_loendur>=3:
                tulemus['O']+=1
                
                
    for i in range(4):
        for j in range(4):
            X_loendur=0
            O_loendur=0
            r=0
            v=0
            while True:
                if i+r>3 or j+v>3 or v>2 or r>2:
                    break
                if maatriks[i+r][j+v]=='X':
                    X_loendur+=1
                    O_loendur=0
                elif maatriks[i+r][j+v]=='O':
                    O_loendur+=1
                    X_loendur=0
                else:
                    X_loendur=0
                    O_loendur=0
                if X_loendur==3:
                    tulemus['X']+=1
                if O_loendur==3:
                    tulemus['O']+=1
                r+=1
                v+=1
        
    for i in range(4):
        for j in range(4):
            X_loendur=0
            O_loendur=0
            r=0
            v=0
            while True:
                if i+v>3 or j-r<0 or v>2 or r>2:
                    break
                if maatriks[i+v][j-r]=='X':
                    X_loendur+=1
                    O_loendur=0
                elif maatriks[i+v][j-r]=='O':
                    O_loendur+=1
                    X_loendur=0
                else:
                    X_loendur=0
                    O_loendur=0
                if X_loendur==3:
                    tulemus['X']+=1
                if O_loendur==3:
                    tulemus['O']+=1
                r+=1
                v+=1
    return tulemus
                

