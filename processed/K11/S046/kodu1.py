
def seosta_lapsed_ja_vanemad(fail1,fail2):
    f = open(fail1,"r",encoding="utf-8")
    f2 = open(fail2,"r",encoding="utf-8")
    isikukoodid = []
    isiknimi = {}
    vastus = {}

    for rida in f2:
        niminr = rida.strip("\n").split(" ",1)
        isiknimi[niminr[0]] = niminr[1]

    for rida in f:
        koodid = rida.strip("\n").split(" ")
        isikukoodid.append([isiknimi[koodid[1]],isiknimi[koodid[0]]])

    for rida in isikukoodid:
        vastus[rida[0]]=set()
        
    for rida in isikukoodid:
        vastus[rida[0]].add(rida[1])
    return(vastus)


