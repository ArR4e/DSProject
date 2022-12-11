def moos(suur, väike, kilod):
    suur_kasutatud_karpe = 0
    väike_kasutatud_karpe = 0
    
    while int(kilod) > 0:
        if kilod >=5 and int(suur) > 0:
            kilod_uus = kilod - 5
            suur_uus = suur - 1
            suur = suur_uus
            suur_kasutatud_karpe += 1
            kilod = kilod_uus
            if kilod_uus == 0:
                break
            continue
        else:
            if int(väike) > 0:
                kilod_uus = kilod - 1
                väike_uus = väike - 1
                väike = väike_uus
                väike_kasutatud_karpe += 1
                kilod = kilod_uus
                if kilod_uus == 0:
                    break
            else:
                break

            
    if kilod == 0:
        return (suur_kasutatud_karpe + väike_kasutatud_karpe)
    else:
        return (-1)
a=2
b=6
c=14
moos(a, b, c)