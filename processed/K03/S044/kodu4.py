fail = open("kinganumbrid.txt", encoding="UTF-8")
sisu = open("kinganumbrid.txt", "r").readlines()
xd = []
for arv in sisu:
    xd.append(arv.split())
fail.close()

for arv in xd:
    if arv != "":
        print(round(2/3 * (arv - 2)))
    else:
        pass
