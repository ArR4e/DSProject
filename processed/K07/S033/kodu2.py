f = open("taksohinnad.txt", encoding = "ISO-8859-1")

teepikkus = float(input('Sisesta tee pikkus kilomeetrites: '))
järjend = []

for rida in f:
    rida = rida.strip()
    järjend.append(rida)

odavaim = ""
maksumus = 9999999
for i in järjend:
    i = i.split(',')
    hind = float(i[1]) + teepikkus * float(i[2])
    if hind < maksumus:
        maksumus = hind
        odavaim = i[0]


print("Kõige odavam on", odavaim)

f.close()
