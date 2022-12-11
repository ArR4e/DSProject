
def max_tulba_järgi(jrnd, n):
    maksimum = 0
    idx = 0
    for i in range(len(jrnd)):
        if jrnd[i][n] > maksimum:
            maksimum = jrnd[i][n]
            idx = i
    return idx

sõidud = []
with open(input("Sisesta failinimi: "), "r") as fail:
    for rida in fail:
        sõidud.append(rida.split())

sõidud_min = []

for i, sõit in enumerate(sõidud):
    tegurid1 = sõit[0].split(":")
    väljumine = int(tegurid1[0]) * 60 + int(tegurid1[1])
    tegurid2 = sõit[1].split(":")
    saabumine = int(tegurid2[0]) * 60 + int(tegurid2[1])
    delta = saabumine - väljumine
    sõidud_min.append((i, saabumine, väljumine, int(sõit[2]), delta))

# eemalda kõige suurema saabumis-väljumis deltaga element
sõidud_min.remove(sõidud_min[max_tulba_järgi(sõidud_min, 4)])
# eemalda kõige suurema hinnaga element
sõidud_min.remove(sõidud_min[max_tulba_järgi(sõidud_min, 3)])

print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ")
for sõit in sõidud_min:
    print(" ".join(sõidud[sõit[0]]))
