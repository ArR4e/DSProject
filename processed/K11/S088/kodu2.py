def transponeeriK(m):
    kokku = []
    for n in range(1, len(m[0])+1):
        r = []
        for i in range(1,len(m)+1):
             r.append(m[-i][-n])
        kokku.append(r)
    return kokku