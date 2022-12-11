def sõidu_hind(sisseistumise_hind, km_hind, tee_pikkus):
    return((km_hind*tee_pikkus+sisseistumise_hind))

odavaim = ["taksonimi", 100000000]
km = float(input("Sisesta teepikkus koduni: "))
f = open("taksohinnad.txt", encoding="UTF-8")
for rida in f:
    loetav_rida = rida.strip("\n").split(",")
    if sõidu_hind(float(loetav_rida[1]),float(loetav_rida[2]),km) < odavaim[1]:
        odavaim[0] = loetav_rida[0]
        odavaim[1] = sõidu_hind(float(loetav_rida[1]),float(loetav_rida[2]),km)

f.close()
print("Kõige odavam on", odavaim[0])