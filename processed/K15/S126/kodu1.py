import re
fail = open("aadressid.txt", "r", encoding = "utf-8")
print("Kasutajanimed on: ")

for jätkuv in fail:
    otsin = re.search("ut.ee/~", jätkuv)
    if (otsin):
        jätk = re.split("~", jätkuv)
        tükid = re.split("/", jätkuv)
        kodukataloog = (tükid[3])
        kasutajanimi = (kodukataloog[1:])
        print(kasutajanimi)
    