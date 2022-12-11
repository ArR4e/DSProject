def transponeeriK(maatriks):
    tmaatriks = []
    a_list = []
    x = len(maatriks)-1
    y = len(maatriks[x])-1
    while True:
        a_list.append(maatriks[x][y])
        #print(maatriks[x][y])
        if x == 0:
            y-=1
            tmaatriks.append(a_list)
            print(a_list)
            a_list = []
            if y == -1:
                break
            else:
                x = len(maatriks)
        x-=1
    return tmaatriks
            