import re
fail = open("aadressid.txt", encoding="UTF-8")
print("Kasutajanimed on: ")
for rida in fail:
    if re.search("http://www.ut.ee/~(\w+)", rida):
            var = re.search("~(\w+)", rida)
            kasutajanimi = re.search("(\w+)", var.group())
            print(kasutajanimi.group())
