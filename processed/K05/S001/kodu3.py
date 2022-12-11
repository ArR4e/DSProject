def moos(suur, vaike, maht):
    karp = 0
    while suur > 0:
        if maht >= 5:
            maht -= 5
            suur -= 1
            karp += 1
        else:
            break
    while vaike > 0:
        if maht >= 1:
            maht -= 1
            vaike -= 1
            karp += 1
        else:
            break
    if maht == 0:
        return karp
    else:
        return -1
    