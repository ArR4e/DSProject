

f = open("aadressid.txt", encoding="utf=8")


print(" Kasutajanimed on:")
for rida in f:
    if "~" in rida and "www.ut.ee" in rida:
        x = rida.strip().split("/")
        y = x[3]
        uus = y.split("~")
        nimi = uus[1]
        print(nimi)

