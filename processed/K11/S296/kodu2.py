def transponeeriK(m):
    mt = []
    if len(m[0]) == len(m):#ruutmaatriks
        for j in range(-1,-(len(m)+1),-1):
            mt_rida = []
            for i in range(-1,-(len(m[j])+1),-1):
                mt_rida.append(m[i][j])
            mt.append(mt_rida)
        return mt

    if len(m[0]) != len(m):#mitte ruutmaatriks
        for j in range(-1,-(len(m[0])+1),-1):
             mt_rida = []
             for i in range(-1,-(len(m)+1),-1):
                 mt_rida.append(m[i][j])
             mt.append(mt_rida)
        return mt
             
            

