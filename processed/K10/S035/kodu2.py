def võitja(maatriks):
    o=0
    x=0
    for i in range(4):
        for j in range(4):
            if maatriks[i] [j]=="X":
                if j<2 and maatriks[i] [j+1]=="X":
                    if maatriks[i] [j+2]=="X":
                        x+=1
                if i<2 and maatriks[i+1] [j]=="X":
                    if maatriks[i+2] [j]=="X":
                        x+=1
                if j<2 and i<2 and maatriks[i+1] [j+1]=="X":
                    if maatriks[i+2] [j+2]=="X":
                        x+=1
                if j>1 and i<2 and maatriks[i+1] [j-1]=="X":
                    if maatriks[i-2] [j-2]=="X":
                        x+=1

            elif maatriks[i] [j]=="O":
                if j<2 and maatriks[i] [j+1]=="O":
                    if maatriks[i] [j+2]=="O":
                        o+=1
                if i<2 and  maatriks[i+1] [j]=="O":
                    if maatriks [i+2] [j]=="O":
                        o+=1
                if j<2 and i<2 and maatriks[i+1] [j+1]=="O":
                    if maatriks[i+2] [j+2]=="O":
                        o+=1
                if j>1 and  i<2 and maatriks[i+1] [j-1]=="O":
                    if maatriks[i-2] [j-2]=="O":
                        o+=1
    seis={"O" : o, "X" : x}
    return(seis)

                

                

                

                    


                   