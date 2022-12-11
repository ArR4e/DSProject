#Kirjuta programm, mis loeb tekstifailist kinganumbrid.txt sisse EU kinganumbrid ja kuvab ekraanile
#vastavad jalalaba pikkused sentimeetrites ümardatuna täisarvuks. Valem jalalaba pikkuse arvutamiseks
#on: pikkus = 2/3 * (kinganumber - 2).

f = open("kinganumbrid.txt")

for rida in f:
    try:
        kinganumber = float(rida.strip())
        pikkus = 2 / 3 * (kinganumber - 2)
        print(round(pikkus))
    except:
        print("Vigane sisend")
    
f.close()