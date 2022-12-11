def võitja(maatriks):
    x_kokku = 0
    x_skoor = 0
    o_kokku = 0
    o_skoor = 0
    skoor = {}
    for y,i in enumerate(maatriks):
        for z,j in enumerate(i):
            if j == "X":
                x_kokku+=1
                q = 1
                while q != 3:#niagonaalis(paremalt-alla vasakule)
                    try:
                        if z-q < 0:
                            break
                        if maatriks[y+q][z-q] == "X":
                            x_kokku+=1
                            
                    except:
                        pass
                    q+=1
                if x_kokku == 3:
                    x_skoor+=1
                    x_kokku = 1
                q = 1
                while q != 3: #ülevalt alla
                    try:
                        if maatriks[y+q][z] == "X":
                            x_kokku+=1
                    except:
                        pass
                    q+=1
                if x_kokku == 3:
                    x_skoor+=1
                    x_kokku = 1
                else:
                    x_kokku = 1
                q = 1
                while q != 3: #diagonaali(vasakult-paremale alla)
                    try:
                        if maatriks[y+q][z+q] == "X":
                            x_kokku+=1
                    except:
                        pass
                    q+=1
                if x_kokku == 3:
                    x_skoor+=1
                    x_kokku = 1
                else:
                    x_kokku = 1
                q = 1
                while q != 3: #vertikaalselt
                    try:
                        if maatriks[y][z+q] == "X":
                            x_kokku+=1
                    except:
                        if x_kokku != 3:
                            x_kokku = 1
                        pass
                    q+=1
                if x_kokku == 3:
                    x_skoor+=1
                x_kokku = 0
            elif j == "O":
                o_kokku+=1
                q = 1
                while q != 3:#niagonaalis(paremalt-alla vasakule)
                    try:
                        if z-q < 0:
                            break
                        if maatriks[y+q][z-q] == "O":
                            o_kokku+=1
                            
                    except:
                        if o_kokku != 3:
                            o_kokku = 1
                        pass
                    q+=1
                if o_kokku == 3:
                    o_skoor+=1
                    o_kokku = 1
                else:
                    o_kokku = 1
                q = 1
                while q != 3: #ülevalt alla
                    try:
                        if maatriks[y+q][z] == "O":
                            o_kokku+=1
                    except:
                        if o_kokku != 3:
                            o_kokku = 1
                        pass
                    q+=1
                if o_kokku == 3:
                    o_skoor+=1
                    o_kokku = 1
                else:
                    o_kokku = 1
                q = 1
                while q != 3: #diagonaali(vasakult-paremale alla)
                    try:
                        if maatriks[y+q][z+q] == "O":
                            o_kokku+=1
                    except:
                        if o_kokku != 3:
                            o_kokku = 1
                        pass
                    q+=1
                if o_kokku == 3:
                    o_skoor+=1
                    o_kokku = 1
                else:
                    o_kokku = 1
                q = 1
                while q != 3: #vertikaalselt
                    try:
                        if maatriks[y][z+q] == "O":
                            o_kokku+=1
                    except:
                        pass
                    q+=1
                if o_kokku == 3:
                    o_skoor+=1
                o_kokku = 0
    skoor["X"] = x_skoor
    skoor["O"] = o_skoor
    return skoor

m = [["X","X","X","X"],
    ["X","X","X","X"],
    ["","","",""],
    ["","","",""]]

print(võitja(m))
