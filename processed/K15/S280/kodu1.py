# 1. Regulaaravaldis / RP

from re import *
fail = open("aadressid.txt", encoding="UTF-8")

print("Kasutajanimed on:")
for rida in fail:
    try:
        rida = rida.strip()
        leht = search("^http://www.ut.ee/", rida)
        if leht:
            vahemik = search("\B~\w+", rida).span()
            print(rida[vahemik[0]+1:vahemik[-1]])
    except:
        pass
    
fail.close()