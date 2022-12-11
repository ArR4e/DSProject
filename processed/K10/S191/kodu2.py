def skoor(i):
    if i=="X":
        x+=1
    else:
        o+=1
def võitja(maatriks):
    x=0
    o=0
    rida=0
    while rida<4:
        veerg=0
        for i in maatriks[rida]:
            if i=="X" or i=="O":
                #print(i,end=" ")
                if veerg<2:
                    if maatriks[rida][veerg+1]==i and maatriks[rida][veerg+2]==i:
                        if i=="X":
                            x+=1
                        else:
                            o+=1
                    if rida<2 and maatriks[rida+1][veerg+1]==i and maatriks[rida+2][veerg+2]==i:
                        if i=="X":
                            x+=1
                        else:
                            o+=1
                if rida<2:
                    if maatriks[rida+1][veerg]==i and maatriks[rida+2][veerg]==i:
                        if i=="X":
                            x+=1
                        else:
                            o+=1
                    if veerg>1 and maatriks[rida+1][veerg-1]==i and maatriks[rida+2][veerg-2]==i:
                        if i=="X":
                            x+=1
                        else:
                            o+=1
            veerg+=1
        rida+=1
    print({"X":x,"O":o})
    return {"X":x,"O":o}
    
võitja([['O',' ',' ','X'],
        [' ','O','X',' '],
        [' ','X','O',' '],
        ['X',' ',' ','O']])