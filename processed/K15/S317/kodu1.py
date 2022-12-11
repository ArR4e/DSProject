import re
fail = open("aadressid.txt", "r", encoding="UTF-8")
print("Kasutajanimed on:")
for i in fail:
    i = i.strip()
    kasutajanimi = re.findall(r"/~[a-z0-9]+", i)
    if kasutajanimi != [] and "http://www.ut.ee" in i:
        print(kasutajanimi[0].strip("/").strip("~"))
fail.close()