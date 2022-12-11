#kodu2 - taksohinnad
teepikkus = float(input("Sisesta kodutee pikkus kilomeetrites: "))
f = open("taksohinnad.txt", encoding = "UTF-8")
nimed = []
taksohinnad = []
for i in f:
    rida = i.strip().split(",")
    nimi = rida[0]
    sisseistumishind = float(rida[1])
    km_hind = float(rida[2])
    hind = sisseistumishind + teepikkus*km_hind
    nimed.append(nimi)
    taksohinnad.append(hind)
    odavaim = min(taksohinnad)
    odavaim_takso = nimed[taksohinnad.index(odavaim)]
print("Odavaim takso on", odavaim_takso)