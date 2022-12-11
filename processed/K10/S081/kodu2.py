import numpy as np

def võitja(a):
    def test(xid,odd):
        xreas = 0
        oreas = 0
        if xid > 2:
            xreas+=1
        if xid == 4:
            xreas+=1
        if odd > 2:
            oreas+=1
        if odd ==4:
            oreas+=1
        return ([xreas,oreas])
    xreas = 0
    oreas = 0
    read = a
    veerud = [[read[j][i] for j in range(len(read))] for i in range(len(read[0]))]
    diagonaalid = [[read[0][0],read[1][1],read[2][2],read[3][3]],
                   [read[1][0],read[2][1],read[3][2]],
                   [read[0][1],read[1][2],read[2][3]],
                   [read[0][3],read[1][2],read[2][1],read[3][0]],
                   [read[1][3],read[2][2],read[3][1]],
                   [read[0][2],read[1][1],read[2][0]]]
    read = read + veerud + diagonaalid
    for i in range(len(read)):
        #saab ette listi ehk rea
        x=0
        o=0
        reap = len(read[i])
        if reap == 4:
            if read[i][0] == 'X' and read[i][1] == 'X' and read[i][2] == 'X': #or read[i][1] == 'X' and read[i][2] == 'X' andread[i][3] == 'X':
                x = read[i].count('X')
                o=0
            elif read[i][1] == 'X' and read[i][2] == 'X' and read[i][3] == 'X':
                x = read[i].count('X')
                o=0
            elif read[i][0] == 'O' and read[i][1] == 'O' and read[i][2] == 'O': #or read[i][1] == 'O' and read[i][2] == 'O' andread[i][3] == 'O':
                o = read[i].count('O')
                x=0
            elif read[i][1] == 'O' and read[i][2] == 'O' and read[i][3] == 'O':
                o = read[i].count('O')
                x=0
        else:   
            x = read[i].count('X')
            o = read[i].count('O')
        xo = test(x,o)
        xreas += xo[0]
        oreas += xo[1]
    
    return({'O':oreas, 'X':xreas})
    

mng = [['X','X','X','O'],
       ['O','X',' ','O'],
       [' ','O','X','O'],
       ['O','O','O','X']]

print(võitja(mng))
