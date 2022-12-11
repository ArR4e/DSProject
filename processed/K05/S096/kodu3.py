# Moosi keetmine

def moos(suur_karp, väike_karp, kogus):
    karbid = 0
    suur = suur_karp
    väike = väike_karp
    kogus = kogus
    if suur*5 + väike*1 >= kogus:
        while kogus > 0:
            if suur > 0 and kogus // 5 > 0 and kogus > 0:
                karbid += 1
                suur -= 1
                kogus -= 5
            elif väike > 0 and väike >= kogus and kogus > 0:
                karbid += 1
                väike -= 1
                kogus -= 1
            else:
                return -1
        return karbid
    else:
        return -1


print(moos(0, 8, 9))