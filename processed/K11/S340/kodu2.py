def transponeeriK(m):
    tmaatriks=[]
    for rida in range(len(m[0]),0,-1):
        liige=[]
        for veerg in range(len(m),0,-1):
            asi=m[veerg-1][rida-1]
            liige.append(asi)
        tmaatriks.append(liige)
    return tmaatriks
