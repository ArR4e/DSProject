maatriks=[['O',' ',' ','X'],
            [' ','O','X',' '],
            [' ','X','O',' '],
            ['X',' ',' ','O']]
def võitja(maatriks):
    X_loendur=0
    O_loendur=0
    vastus={}
    vastus['X']=0
    vastus['O']=0
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
                vastus['X']+=1
            if O_loendur>=3:
                vastus['O']+=1
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
                vastus['X']+=1
            if O_loendur>=3:
                vastus['O']+=1
    
    for i in range(4):
        for j in range(4):
            X_loendur=0
            O_loendur=0
            l=0
            c=0
            while True:
                if i+l>3 or j+c>3 or c>2 or l>2:
                    break
                if maatriks [i+l][j+c]=='X':
                    X_loendur+=1
                    O_loendur=0
                elif maatriks [i+l][j+c]=='O':
                    O_loendur+=1
                    X_loendur=0
                else:
                    X_loendur=0
                    O_loendur=0
                
                if X_loendur>=3:
                    vastus['X']+=1
                if O_loendur>=3:
                    vastus['O']+=1
                l+=1
                c+=1
    for i in range(4):
        for j in range(4):
            X_loendur=0
            O_loendur=0
            l=0
            c=0
            while True:
                if i+c>3 or j-l>3 or c>2 or l>2:
                    break
                if maatriks [i+c][j-l]=='X':
                    X_loendur+=1
                    O_loendur=0
                elif maatriks [i+c][j-c]=='O':
                    O_loendur+=1
                    X_loendur=0
                else:
                    X_loendur=0
                    O_loendur=0
                
                if X_loendur>=3:
                    vastus['X']+=1
                if O_loendur>=3:
                    vastus['O']+=1
                l+=1
                c+=1            
    return vastus
            
print(võitja(maatriks))