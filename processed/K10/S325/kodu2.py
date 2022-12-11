def võitja(l):
    d=dict({"O":0,"X":0})
    for j in range(2):
        for i in range(4):
            if l[i][j]==l[i][j+1]==l[i][j+2]:
                if l[i][j]=="X" or l[i][j]=="O":
                    d[l[i][j]]+=1
            if l[j][i]==l[j+1][i]==l[j+2][i]:
                if l[j][i]=="X" or l[j][i]=="O":
                    d[l[j][i]]+=1
        for i in range(2):
            if l[j][i]==l[j+1][i+1]==l[j+2][i+2]:
                if l[j][i]=="X" or l[j][i]=="O":
                    d[l[j][i]]+=1
        for i in range(2,4):
            if l[i][j]==l[i-1][j+1]==l[i-2][j+2]:
                if l[i][j]=="X" or l[i][j]=="O":
                    d[l[i][j]]+=1
        
    return d
