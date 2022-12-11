teepikkus = input("Sisesta tee pikkus kilomeetrites: ")
odavaim_pakkumine = 90000000000000000000000000000000000

f = open('taksohinnad.txt')
for rida in f:
    rida = rida.strip()
    rida = rida.split(',')
    hind = float(rida[1]) + float(rida[2]) * float(teepikkus)
    firma = rida[0]
    if hind < odavaim_pakkumine:
        odavaim_pakkumine = hind
        odavaim_firma = firma

print("Kõige odavam on " + odavaim_firma + ".")

f.close()