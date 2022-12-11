import re

f=open("aadressid.txt",encoding="UTF-8")

print("Kasutajanimed on:")
for rida in f:
    rida=rida.strip()
    if re.match("http://www.ut.ee/~",rida):
        index=rida.index("~")
        nimealgus=(rida[index+1:])
        for el in nimealgus:
            if el=="/":
                nimi=nimealgus[:nimealgus.index(el)]
                print(nimi)
                break
f.close()