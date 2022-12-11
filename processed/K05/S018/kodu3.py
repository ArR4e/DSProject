def moos(s, v, m):
    väike = int(v)
    suur = int(s)
    mass = int(m)
    karp = 0
    kogu_v = suur*5 + väike
    while True:
        if mass > kogu_v or (mass < 5 and mass > väike):
            karp = -1
            break
        else:
            if mass >= 5 and suur > 0:
                karp += 1
                suur -= 1
                mass -= 5
            elif (mass < 5 or suur == 0) and mass >= 1 and väike > 0:
                karp += 1
                väike -= 1
                mass -= 1
            else:
                break
    return(karp)