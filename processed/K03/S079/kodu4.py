# 4. Erindite püüdmine failist lugemisel
# Kirjuta programm, mis loeb tekstifailist kinganumbrid.txt sisse EU kinganumbrid ja
# kuvab ekraanile vastavad jalalaba pikkused sentimeetrites ümardatuna täisarvuks.
# Valem jalalaba pikkuse arvutamiseks on: pikkus = 2/3 * (kinganumber - 2).

# Faili nende ridade juures, kus arvuks teisendamine miskipärast ebaõnnestub,
# tuleb ekraanile kuvada „Vigane sisend” ning jätkata faili järgmise reaga.

#failinimi = input("Sisesta failinimi: ")
failinimi = "kinganumbrid.txt"
f = open(failinimi)

while True:
    EU = f.readline()
    if EU == "":
        break
    else:
        try:
            EU = float(EU)
            pikkus = round(2/3 * (EU-2))
            print(pikkus)
        except:
            print("Vigane sisend")
    