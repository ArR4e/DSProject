def transponeeriK(maatriks):
    t_maatriks = []
    for i in range(len(maatriks)-1,-1,-1):
        t_maatriks_r = []
        for j in range((len(maatriks[0])-1),-1,-1):
            t_maatriks_r += [maatriks[i][j]]
        t_maatriks += [t_maatriks_r]
    
    jär1 = []
    jär_trans = []
    i1 = 0
    j1 = 0
    while True:
        if i1 >= len(t_maatriks):
            i1 = 0
            j1 += 1
        if j1 >= len(t_maatriks[0]):
            break
        jär1.append(t_maatriks[i1][j1])
        i1 += 1
        if len(jär1) == len(t_maatriks):
            jär_trans.append(jär1)
            jär1 = []
    return jär_trans