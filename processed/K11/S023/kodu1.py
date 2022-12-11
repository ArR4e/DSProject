



def seosta_lapsed_ja_vanemad(fail1,fail2):
    fail1 = open(fail1)
    fail2 = open(fail2)
    nimed = {}
    vanemad_lapsed = {}
    for i in fail2:
        i = i.strip()
        i = i.split(" ")
        nimed[i[0]] = i[1:]
    for j in fail1:
        j = j.strip()
        j = j.split(" ")
        nimi1 = ""
        nimi2 = ""
        for k in range(len(nimed[j[0]])):
            if k == 0:
                nimi1 = nimi1 + nimed[j[0]][k]
            else:
                nimi1 = nimi1 + " " + nimed[j[0]][k]
        for k in range(len(nimed[j[1]])):
            if k == 0:
                nimi2 = nimi2 + nimed[j[1]][k]
            else:
                nimi2 = nimi2 + " " + nimed[j[1]][k]
        try:
            eelmine = vanemad_lapsed[nimi2]
        except:
            eelmine = ""
        if eelmine == "":
            vanemad_lapsed[nimi2] = [nimi1]
        else:
            vanemad_lapsed[nimi2] =eelmine + [nimi1]
    return vanemad_lapsed

sõnaraamat = seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt")

for i in sõnaraamat:
    if len(sõnaraamat[i]) == 1:
        print(i,":",sõnaraamat[i][0])
    else:
        print(i,":",sõnaraamat[i][0],",",sõnaraamat[i][1])
    
    

