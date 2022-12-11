def failist_lugemine(faili_nimi):
    f=open(faili_nimi, encoding = "utf-8")
    read = []
    for rida in f:
        read.append(rida.strip())
    f.close()
    return read

def isikukoodid_nimedeks(nimed):
    nimed_failist = failist_lugemine(nimed)
    nimed = {}
    for element in nimed_failist:
        isikukood_ja_nimi = element.split()
        nimi = isikukood_ja_nimi[1]+ " " + isikukood_ja_nimi[2]
        isikukood = isikukood_ja_nimi[0]
        nimed[isikukood] = nimi
        
    return nimed
   
def seosta_lapsed_ja_vanemad(lapsed, nimed):
    lapsed_failist = failist_lugemine(lapsed)
    nimed = isikukoodid_nimedeks(nimed)
    lapsed = {}
    for element in lapsed_failist:
        laps_ja_vanem = element.split()
        laps = nimed[laps_ja_vanem[1]]
        vanem = nimed[laps_ja_vanem[0]]
        
        if laps in lapsed:
            lapsed[laps].add(vanem)
        else:
            lapsed[laps] = set()
            lapsed[laps].add(vanem)
            
    return lapsed

# def prindi_read(lapsed):
#     for laps in lapsed:
#         rida = laps + ": " + ", ".join(lapsed[laps])
#         print(rida)
    

    
    
    

