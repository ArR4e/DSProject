fail = open("kinganumbrid.txt", "r", encoding="utf-8")
tekst = fail.readlines()
uus_tekst = []
for x in tekst:
    try:
        uus_tekst += [round(2/3 * (float(x)-2))]
    except:
        uus_tekst += ["Vigane sisend"]
fail.close()

for x in uus_tekst:
    print(x)