pikkus = float(input("Sisesta tee pikkus (km): "))
f = open("taksohinnad.txt", "r")

järjend1 = []
järjend2 = []
try:
    for rida in f:
        rida_uus = rida.split(",")
        hind = float(rida_uus[1]) + float(rida_uus[2].strip()) * pikkus
        järjend1 += [hind]
        järjend2 += [rida_uus[0]]
        odavaim = min(järjend1)
    takso = järjend2[järjend1.index(odavaim)]
    print("Kõige odavam takso on " + takso + ".")
except:
    print("Taksod puuduvad.")
f.close()