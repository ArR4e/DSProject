def seosta_lapsed_ja_vanemad(fail1,fail2):
    lapsed = open(fail1,encoding='Utf-8')
    nimed = open(fail2,encoding='Utf-8')
    sõnastik = {}
    laps = []
    vanem = []
    for rida in lapsed:
        #rida = rida.strip().split()
        nimed.seek(0)
        vanem = []
        for rida2 in nimed:
            #rida = rida.split()
            
            rida2 = rida2.strip().split()
            if (rida.split())[0] == rida2[0]:
                vanemn = (rida2[1]+' '+rida2[2])
                vanem.append(vanemn)
                
            if (rida.split()[1]) == rida2[0]:
                lapsn = rida2[1]+' '+rida2[2]
                #laps.append(lapsn)
        if lapsn in sõnastik.keys():            
            sõnastik[lapsn].append(vanem)
        else:
            sõnastik[lapsn] = vanem
        t = sõnastik.values()
        
    return (sõnastik)
    lapsed.close()
    nimed.close()
print(seosta_lapsed_ja_vanemad('lapsed.txt','nimed.txt'))
            
