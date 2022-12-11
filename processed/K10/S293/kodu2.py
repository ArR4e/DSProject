import numpy
x=[['O',' ','O','X'],
            ['O','O','X','X'],
            ['O','X','O',' '],
            ['X','X','X','O']]


def võitja(x):
    lõpp={}
    Xh=0
    Oh=0
    Xv=0
    Ov=0
    Xd=0
    Od=0
    Xd2=0
    Od2=0
    x1=0
    x2=3
    o1=0
    o2=3
    xd=[""]*4
    xd2=[""]*4
    od=[""]*4
    od2=[""]*4
    xtrans=numpy.transpose(x)
    for i in x:
        if i[0]=="X" and i[1]=="X" and i[2]=="X":
            Xh+=1
        if i[1]=="X" and i[2]=="X" and i[3]=="X":
            Xh+=1
        if i[0]=="O" and i[1]=="O" and i[2]=="O":
            Oh+=1
        if i[1]=="O" and i[2]=="O" and i[3]=="O":
            Oh+=1
    for i in xtrans:
        if i[0]=="X" and i[1]=="X" and i[2]=="X":
            Xv+=1
        if i[1]=="X" and i[2]=="X" and i[3]=="X":
            Xv+=1
        if i[0]=="O" and i[1]=="O" and i[2]=="O":
            Ov+=1
        if i[1]=="O" and i[2]=="O" and i[3]=="O":
            Ov+=1
    for i in x:
        if i[x1]=="X":
            xd[x1]=i[x1]
        x1+=1
    for i in x:
        if i[x2]=="X":
            xd2[x2]=i[x2]
        x2-=1
    for i in x:
        if i[o1]=="O":
            od[o1]=i[o1]
        o1+=1
    for i in x:
        if i[o2]=="O":
            od2[o2]=i[o2]
        o2-=1
    
    if xd[0]=="X" and xd[1]=="X" and xd[2]=="X":
        Xd+=1
    if xd[1]=="X" and xd[2]=="X" and xd[3]=="X":
        Xd+=1
    if od[0]=="O" and od[1]=="O" and od[2]=="O":
        Od+=1
    if od[1]=="O" and od[2]=="O" and od[3]=="O":
        Od+=1
    if xd2[0]=="X" and xd2[1]=="X" and xd2[2]=="X":
        Xd2+=1
    if xd2[1]=="X" and xd2[2]=="X" and xd2[3]=="X":
        Xd2+=1
    if od2[0]=="O" and od2[1]=="O" and od2[2]=="O":
        Od2+=1
    if od2[1]=="O" and od2[2]=="O" and od2[3]=="O":
        Od2+=1
        
    if x[0][1]=="X" and x[1][2]=="X" and x[2][3]=="X":
        Xd+=1
    if x[0][1]=="O" and x[1][2]=="O" and x[2][3]=="O":
        Od+=1
    if x[1][0]=="X" and x[2][1]=="X" and x[3][2]=="X":
        Xd+=1
    if x[1][0]=="O" and x[2][1]=="O" and x[3][2]=="O":
        Od+=1
    if x[2][0]=="X" and x[1][1]=="X" and x[0][2]=="X":
        Xd+=1
    if x[2][0]=="O" and x[1][1]=="O" and x[0][2]=="O":
        Od+=1
    if x[3][1]=="X" and x[2][2]=="X" and x[1][3]=="X":
        Xd+=1
    if x[3][1]=="O" and x[2][2]=="O" and x[1][3]=="O":
        Od+=1
         
    
    osum=Ov+Oh+Od+Od2
    xsum=Xv+Xh+Xd+Xd2
    lõpp["O"]=osum
    lõpp["X"]=xsum
    return(lõpp)
print(võitja(x))