def võitja(maatriks):
    x_lugeja=0
    o_lugeja=0
    x_diag=0
    o_diag=0
    for i in range(4):
        for j in range(2):
            if maatriks[i][j]==maatriks[i][j+1]==maatriks[i][j+2]=='X':
                x_lugeja+=1
            if maatriks[i][j]==maatriks[i][j+1]==maatriks[i][j+2]=='O':
                o_lugeja+=1
    for i in range(2):
        for j in range(4):
            if maatriks[i][j]==maatriks[i+1][j]==maatriks[i+2][j]=='X':
                x_lugeja+=1
            if maatriks[i][j]==maatriks[i+1][j]==maatriks[i+2][j]=='O':
                o_lugeja+=1
    for i in range(2):
        for j in range(2):
            if maatriks[i][j]==maatriks[i+1][j+1]==maatriks[i+2][j+2]=='X':
                x_lugeja+=1
            if maatriks[i][j]==maatriks[i+1][j+1]==maatriks[i+2][j+2]=='O':
                o_lugeja+=1
    for i in range(2):
        for j in range(2):
            if maatriks[i][j+2]==maatriks[i+1][j+1]==maatriks[i+2][j]=='X':
                x_lugeja+=1
            if maatriks[i][j+2]==maatriks[i+1][j+1]==maatriks[i+2][j]=='O':
                o_lugeja+=1
    tulemus={}
    tulemus['X']=x_lugeja
    tulemus['O']=o_lugeja
    return tulemus