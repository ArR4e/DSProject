def võitja(maatriks):
    järjest_3={'O':0,'X':0}
    for i in range(len(maatriks)):
        x=[]
        y=[]
        for j in range(len(maatriks[i])):
            if maatriks[i][j] == 'X':
                x+=[j]
            if maatriks[i][j] == 'O':
                y+=[j]
        if len(x) == 4:
            järjest_3['X']+=2
        elif len(y) == 4:
            järjest_3['O']+=2
        elif len(x)==3:
            if sum(x) ==3 or sum(x)==6:
                järjest_3['X']+=1
        elif len(y)==3: 
            if sum(y) ==3 or sum(y)==6:
                järjest_3['O']+=1
    for i in range(len(maatriks)):
        x=[]
        y=[]
        for j in range(len(maatriks[i])):
            if maatriks[j][i] == 'X':
                x+=[j]
            if maatriks[j][i] == 'O':
                y+=[j]
        if len(x) == 4:
            järjest_3['X']+=2
        elif len(y) == 4:
            järjest_3['O']+=2
        elif len(x)==3:  
            if sum(x) ==3 or sum(x)==6:
                järjest_3['X']+=1
        elif len(y)==3:
            if sum(y) ==3 or sum(y)==6:
                järjest_3['O']+=1
    if maatriks[0][0]==maatriks[1][1]==maatriks[2][2]!=' ':
        järjest_3[maatriks[0][0]]+=1
    if maatriks[1][1]==maatriks[2][2]==maatriks[3][3]!=' ':
        järjest_3[maatriks[1][1]]+=1
    if maatriks[0][1]==maatriks[1][2]==maatriks[2][3]!=' ':
        järjest_3[maatriks[0][1]]+=1
    if maatriks[1][0]==maatriks[2][1]==maatriks[3][2]!=' ':
        järjest_3[maatriks[1][0]]+=1
    if maatriks[0][2]==maatriks[1][1]==maatriks[2][0]!=' ':
        järjest_3[maatriks[0][2]]+=1
    if maatriks[0][3]==maatriks[1][2]==maatriks[2][1]!=' ':
        järjest_3[maatriks[0][3]]+=1
    if maatriks[1][2]==maatriks[2][1]==maatriks[3][0]!=' ':
        järjest_3[maatriks[1][2]]+=1
    if maatriks[1][3]==maatriks[2][2]==maatriks[3][1]!=' ':
        järjest_3[maatriks[1][3]]+=1
    return järjest_3
