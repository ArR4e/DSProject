# 1. Lapsed ja vanemad / RP

def seosta_lapsed_ja_vanemad(lapsefail, nimefail):
    
    vanemaisik = []
    lapseisik = []
    
    lapsed = open(lapsefail, encoding="UTF-8")
    for rida in lapsed:
        asi = rida.strip().split(" ")
        vanemaisik.append(asi[0])
        lapseisik.append(asi[1])
    lapsed.close()
    
    nimed = open(nimefail, encoding="UTF-8")
    for rida in nimed:
        asi = rida.strip().split(" ")
        for i, el in enumerate(vanemaisik):
            if el == asi[0]:
                vanemaisik[i] = asi[1] + " " + asi[2]
        for i, el in enumerate(lapseisik):
            if el == asi[0]:
                lapseisik[i] = asi[1] + " " + asi[2]
    nimed.close()
    
    seosed = {}
   
    for i, el in enumerate(lapseisik):
        if el not in seosed:
            seosed[el] = vanemaisik[i]
        else:
            seosed[el] = {seosed[el], vanemaisik[i]}
            
    for el in seosed:
        if type(seosed[el]) == str:
            seosed[el] = {seosed[el]}
            
    return seosed

gg = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")

for el in gg:
    print(el + ": " + str(gg[el]))