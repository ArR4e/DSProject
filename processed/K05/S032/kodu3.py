def moos(n_suur_kokku, n_väike_kokku, moos_kg):
    n_suur = 0
    n_väike = 0
    if moos_kg > 5*n_suur_kokku + n_väike_kokku:
        return -1
    while n_suur < n_suur_kokku and moos_kg >= 5:
        moos_kg -= 5
        n_suur +=1
    while n_väike < n_väike_kokku and moos_kg > 0:
        moos_kg -= 1
        n_väike +=1    
    if moos_kg == 0:
        return n_suur + n_väike
    else:
        return -1

print(moos(1,0,5))