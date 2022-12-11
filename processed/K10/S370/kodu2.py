def võitja(m):
    tulemus={'O': 0, 'X':0}
    for kes in tulemus:
        for rida in range(4):
            for veerg in range(4):
                try:
                    if m[rida][veerg]==m[rida+1][veerg] ==m[rida+2][veerg] ==kes:
                        tulemus[kes]=tulemus.get(kes,0)+1
                except:
                    pass
                try:
                    if m[rida][veerg]==m[rida][veerg+1] ==m[rida][veerg+2] ==kes:
                        tulemus[kes]=tulemus.get(kes,0)+1
                except:
                    pass
                try:
                    if m[rida][veerg]==m[rida+1][veerg+1] ==m[rida+2][veerg+2] ==kes:
                        tulemus[kes]=tulemus.get(kes,0)+1
                except:
                    pass
                if rida < 2 and veerg >1:
                    try:
                        if m[rida][veerg]==m[rida+1][veerg-1] ==m[rida+2][veerg-2] ==kes:
                            tulemus[kes]=tulemus.get(kes,0)+1
                    except:
                        pass
    return(tulemus)
                    
