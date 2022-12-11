fail = open("taksohinnad.txt", encoding = "UTF")
kodutee_pikkus = int(input("Sisesta kui pikk tee on sinu koduni (kilomeetrites): "))

esimene_rida_loetud = fail.readline()
esimene = esimene_rida_loetud.strip("\n").split(",")
esimene_sõidu_hind = float(esimene[1]) + float(esimene[2])*kodutee_pikkus
eelmine = esimene_sõidu_hind
odavaim_takso = esimene[0]

for rida in fail:
    if rida == "":
        break
    järjend = rida.strip("\n").split(",")
    nimi = järjend[0]
    start = järjend[1]
    kmhind = järjend[2]
    sõidu_hind = float(start) + float(kmhind)*kodutee_pikkus
    if sõidu_hind < eelmine and sõidu_hind < esimene_sõidu_hind:
        odavaim_takso = nimi
    eelmine = sõidu_hind
    
print("Odavaim takso on", str(odavaim_takso) + ".")
fail.close()
        