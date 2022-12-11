taksod = ""
with open("taksohinnad.txt", 'r', encoding = "utf-8") as f:
    taksod = f.readlines()

tee = float(input("sisesta tee pikkus km-tes : "))

n = 0
odavaim = ""
for elem in taksod:
    elem = elem.strip()
    elem = elem.split(",")
    nimi = elem[0]
    sisenemine = float(elem[1])
    kmhind = float(elem[2])
    takso_hind = sisenemine + tee*kmhind
    if n== 0:
        n+= takso_hind
    if takso_hind <= n:
        odavaim = nimi
        n = takso_hind
print(odavaim)