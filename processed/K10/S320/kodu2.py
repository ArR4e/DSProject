def liigu(x,y, loendur, mängija, suund, maatriks):
    if loendur==0:
        return 1
    if  not -1<y<len(maatriks) or not -1<x<len(maatriks[y]) or maatriks[y][x] !=mängija:
        return 0
    return liigu(x+suund[0], y+suund[1], loendur-1, mängija, suund, maatriks)

def võitja(maatriks):
    suunad={"alla":(0,1), "paremale":(1,0), "diagonaal_alla":(1,1), "diagonaal_üles":(1,-1)}
    võti={"X":0, "O":0}
    
    for y in range(len(maatriks)):
        for x in range(len(maatriks[y])):
            for suund in suunad.values():
                võti["X"]=võti["X"]+liigu(x, y, 3, "X", suund, maatriks)
                võti["O"]=võti["O"]+liigu(x, y, 3, "O", suund, maatriks)
                
    return võti        


