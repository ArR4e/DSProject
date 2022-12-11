import re
print("Kasutajanimed on:")
fail = open("aadressid.txt", encoding="UTF-8")
for rida in fail:
    if re.match("http://www.ut.ee/~",rida):
        print(rida[18:22])

