import re

f=open("aadressid.txt", encoding="UTF-8")
for rida in f:
    if re.match(".*http://www.ut.ee/~.*",rida):
        rida=rida.split("/")
        kasutajanimi=rida[3]
        kasutajanimi=list(kasutajanimi)
        kasutajanimi.remove("~")
        kasutajanimi="".join(kasutajanimi)
        print(kasutajanimi)
f.close()