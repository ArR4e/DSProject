#Regulaaravaldis, leiab failist Tartu Ülikooli kasutajanimed
#http://www.ut.ee/~kasutajanimi/...

import re

f = open("aadressid.txt",encoding='UTF-8')
sisu = f.readlines()
f.close()

print("Leiti järgmised kasutajanimed:")

for rida in sisu:
    rida = rida.strip("\n ")
    if re.search("http://www.ut.ee/~(?!\s)\w*?/*",rida):
        nimi = re.search("/~\w*?/",rida)
        print(nimi.group()[2:-1])
