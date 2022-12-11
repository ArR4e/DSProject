g = open("taksohinnad.txt", "r")

teepikkus = float(input("Ma tahan edasi pidutseda, palun aita mul see proge kodutöö ära teha ja sisesta number: "))

taksod = []
hinnad = []
for rida in g.readlines():
    rida = rida.split(",")
    taksod.append(rida[0])
    hinnad.append([float(rida[1]), float(rida[2])])

miinimum = 99999999999999
for hind in hinnad:
    maksumus = hind[0] + teepikkus * hind[1]
    if maksumus < miinimum:
        miinimum = maksumus
        min_maksumus = [hind[0], hind[1]]

odavaim = taksod[hinnad.index(min_maksumus)]
#hinnad = {}
"""hind = 9999999999999
n = 0
for takso in taksod:
    hind1 = float(takso[1]) + teepikkus * float(takso[2])
    if hind1 < hind:
        miinimum = takso[0]
    n += 3
    hind = hind1"""

print(f"Kõige odavam on {odavaim}.")

g.close()