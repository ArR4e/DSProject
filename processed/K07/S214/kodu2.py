fail = open("taksohinnad.txt", encoding = "utf-8")

teepikkus = input("Sisesta tee pikkus kilomeetrites: ")

hinnad = []
nimed = []

for rida in fail:
    järjend = rida.split(",")
    sisseistumise_hind = float(järjend[-2].strip())
    kilomeetri_hind = float(järjend[-1].strip())
    kogu_hind = sisseistumise_hind + kilomeetri_hind * float(teepikkus)
    hinnad += [kogu_hind]
    nimed += järjend[:-2]
try:
    odavaim = min(hinnad)
    indeks = hinnad.index(odavaim)
    nimi = nimed[indeks]
    print("Kõige odavam takso on "+nimi+".")
except:
    a = 0
fail.close()