import re

f = open("aadressid.txt", encoding="UTF-8")

esimene = 0
for rida in f:
    rida = rida.strip(' \t')
    if re.match("http://www.ut.ee/~.*/.*", rida):
        if esimene == 0:
            esimene = 1
            print("Kasutajanimed on:")
        print(rida.lstrip('http://www.ut.ee/').split('/')[0].strip('~'))

if esimene == 0:
    print("Kasutajanimed puuduvad.")
f.close()