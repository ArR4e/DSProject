import re

musterUT = "http://www.ut.ee/..."

with open("aadressid.txt", "r", encoding = "UTF-8") as f:
    print("Kasutajanimed on: ")
    for rida in f:
        if re.match(musterUT, rida.strip()) and "~" in rida.strip():
            kasutajanimi = rida.strip().strip("http://www.ut.ee/~")
            print(kasutajanimi.split("/")[0])