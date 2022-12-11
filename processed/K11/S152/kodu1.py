lapsed = open("lapsed.txt", "r", encoding="UTF=8")
nimed = open("nimed.txt", "r", encoding="UTF=8")
sõnastik={}

def seosta_lapsed_ja_vanemad(lapsed, nimed):
    for rida in lapsed:
        isikukood = rida.strip().split(" ")
        for el in nimed:
            osa = el.strip().split(" ")
            osa[1:3] = [''.join(osa[1:3])] #ma tahtsin siin nagu 1 ja 2 elemendi kokku panna aga siis ma sain aru, et ta paneb nagu nt KadriKalkun kokku niiet see ka veits jama
           # print(osa)
            if isikukood[1] == osa[0] and osa[1] not in sõnastik:
                laps = " ".join(osa[1:])
                    
                nimed_uuesti = open("nimed.txt", encoding="utf=8")
                for i in nimed_uuesti:
                    osa2 = i.strip().split(" ")
                    if isikukood[0] == osa2[0] and laps in sõnastik:
                        sõnastik[laps].append(" ". join(osa2[1:]))
                    elif isikukood[0] == osa2[0] and laps not in sõnastik:
                        sõnastik[laps] = [" ". join(osa2[1:])]
                        print(sõnastik)
    lapsed.close()
    nimed.close()
    for võti, väärtus in sõnastik.items():
        print("{}:{}".format(võti,väärtus))
    return sõnastik
  

seosta_lapsed_ja_vanemad(lapsed, nimed)


    
   

