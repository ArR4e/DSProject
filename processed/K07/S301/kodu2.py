teepikkus = input("Sisesta tee pikkus kilomeetrites: ")
f = open("taksohinnad.txt", encoding = "UTF-8")
rida = 0
odavaim = 99999999
def summa(teepikkus, alustus_tasu, km_hind):
     kokku = float(teepikkus) * km_hind + alustus_tasu
     return kokku
for rida in f:
    rida = rida.split(",")
    pakkuja = rida[0]
    alustus_tasu = float(rida [1])
    km_hind = float(rida[2].strip())
    pakkumine = summa(teepikkus, alustus_tasu, km_hind)
    if pakkumine <= odavaim:
        odavaim = pakkumine
        parim_pakkuja = pakkuja
print(f"Koige odavam on {parim_pakkuja}")