import re
f = open("aadressid.txt")
print("Kasutajanimed on:")
while True:
    rida = f.readline().strip()
    if rida == "":
        break
    kasutajanimi = re.search("www.ut.ee/~(\w+)/", str(rida))
    if kasutajanimi:
        print(kasutajanimi.group(1))
f.close()