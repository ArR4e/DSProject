def moos(suuredk, vaikesedk, kogus):
    suuredk = int(suuredk)
    vaikesedk = int(vaikesedk)
    kogus = int(kogus)
    karpe = 0
    while kogus > 0:
        while suuredk > 0 and kogus >= 5:
                kogus = kogus -5
                karpe = karpe + 1
                suuredk = suuredk -1
        else:
            break
        while vaikesedk > 0 and kogus > 0:
                kogus = kogus -1
                karpe = karpe + 1
                vaikesedk = vaikesedk - 1
        else:
            break
        if kogus > 0:
            karpe = -1
            break
                    
    print(moos(suuredk, vaikesedk, kogus))