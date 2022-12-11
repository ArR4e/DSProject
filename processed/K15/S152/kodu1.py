import re
fail = open("aadressid.txt", encoding = "utf-8")
print("Kasutajanimed on:")
for rida in fail:
    if re.search("http://www.ut.ee/~",rida):
        sisu = rida.split("~")
        nimi_terve = sisu[1]
        ainult_nimi = nimi_terve.split("/")
        nimi = ainult_nimi[0]
        print(nimi)
        

fail.close()   