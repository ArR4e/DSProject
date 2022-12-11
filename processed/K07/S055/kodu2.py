km = float(input("Sisesta tee pikkus kilomeetrites: "))

f = open("taksohinnad.txt", encoding="UTF-8")

taksod = []
summad = []

sisu = f.readlines()

if sisu:
    for rida in sisu:
        a = rida.split(",")
        taksod.append(a[0].strip())
        summad.append(float(a[1]) + float(a[2]) * km)

    print("Kõige odavam on " + taksod[summad.index(min(summad))] + ".")
