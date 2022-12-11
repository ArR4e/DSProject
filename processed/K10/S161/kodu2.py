maatriks=  [['X','X','X',' '],
            [' ','O',' ',' '],
            [' ',' ','O',' '],
            [' ',' ',' ','O']]
def võitja(maatriks):
    x=0
    o=0
    tulemus={}
    for i in maatriks:
        if i[2]!=' ' and i[0]==i[1]==i[2] or i[1]==i[2]==i[3]:
            if i[1]=='O':
                o+=1
            else:
                x+=1
    for i in range(1):
        for j in range(2):
            if maatriks[i+2][j]!=' ' and maatriks[i][j]==maatriks[i+1][j]==maatriks[i+2][j] or maatriks[i+1][j]==maatriks[i+2][j]==maatriks[i+3][j]:
                if maatriks[i+1][j+1]=='O':
                    o+=1
                else:
                    x+=1
            if maatriks[2][2]!=' ' and maatriks[0][0]==maatriks[1][1]==maatriks[2][2] or maatriks[1][1]==maatriks[2][2]==maatriks[3][3]:
                if maatriks[i+1][j+1]=='O':
                    o+=1
                else:
                    x+=1
    if maatriks[1][2]!=' ' and maatriks[0][3]==maatriks[1][2]==maatriks[3][1] or maatriks[1][2]==maatriks[3][1]==maatriks[4][0]:
        if maatriks[1][2]=='O':
            o+=1
        else:
            x+=1
    tulemus['X']=x
    tulemus['O']=o
    return tulemus
print(võitja(maatriks))