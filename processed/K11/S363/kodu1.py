import pprint

def seosta_lapsed_ja_vanemad(lapsed, nimed):
    f1 = open(lapsed, "r")
    f2 = open(nimed, "r", encoding = "UTF-8")
    isikukoodid = {}
    for rida in f2:
        rida = rida.strip().split()
        nimi = ""
        for i in rida[1:]:
            nimi += i + " "
        nimi = nimi[:-1]
        isikukoodid[rida[0]] = nimi
    
    vanemad = {}
    for rida in f1:
        rida = rida.strip().split()
        if rida[1] in vanemad.keys():
            vanemad[rida[1]] = vanemad[rida[1]], rida[0]
        else:
            vanemad[rida[1]] = rida[0]
        
    vanemate_nimed = {}
        
    for laps in vanemad.keys():
        for isik in isikukoodid.keys():
            if isik in vanemad[laps]:
                if isikukoodid[laps] in vanemate_nimed.keys():
                    vanem = vanemate_nimed[isikukoodid[laps]]
                    vanem.add(isikukoodid[isik])
                    vanemate_nimed[isikukoodid[laps]] = vanem
                    
                else:
                    vanem = set()
                    vanem.add(isikukoodid[isik])
                    vanemate_nimed[isikukoodid[laps]] = vanem
    
    return vanemate_nimed

sõnastik = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")
for k in sõnastik.keys():
    prindi = k + ": "
    for vanem in sõnastik[k]:
        prindi = prindi + vanem + ", "
    prindi = prindi[:-2]
    print(prindi)
            
 

        