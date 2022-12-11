from copy import deepcopy
def võitja(a):
    
    t={'X':0, 'O':0, ' ':0}
    for x in range(2):
        print(a)
        for i in range(4):
            e=a[0][i]
            n=0
            for j in range(1,4):
                if e==a[j][i]:
                    n+=1
                elif n==0:
                    e=a[j][i]
                else:
                    break
            if n==3:
                t[e]+=2
            elif n==2:
                t[e]+=1
        
        e=a[0][0]
        n=0
        for j in range(1,4):
            if e==a[j][j]:
                n+=1
            elif n==0:
                n=0
                e=a[j][j]
            else:
                break
        if n==3:
            t[e]+=2
        elif n==2:
            t[e]+=1
        if a[0][1]==a[1][2]==a[2][3]:
            t[a[0][1]]+=1
        if a[1][0]==a[2][1]==a[3][2]:
            t[a[1][0]]+=1
        if x==0:
            b=deepcopy(a)
            for i in range(4):
                for j in range(4):
                    b[3-j][i]=a[i][j]
        a=b
    t.pop(' ')
    return t
print(võitja([[' ', ' ', ' ', 'O'], [' ', 'X', 'O', ' '], [' ', 'O', 'X', ' '], [' ', ' ', ' ', 'X']]))
