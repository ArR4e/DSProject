fail = open("kinganumbrid.txt", encoding = "utf-8")

while True:
    rida = fail.readline()
    if rida == "":
        break
    try:
        kinganumber = float(rida)
        pikkus = round(2/3 * (kinganumber - 2))
        print(pikkus)
    except:
        print("Vigane sisend")
fail.close()

#iga rea kohta eraldi lugeda sisse, tsükkliga, try ja except
#Kirjuta programm, mis loeb tekstifailist kinganumbrid.txt sisse EU kinganumbrid
#ja kuvab ekraanile vastavad jalalaba pikkused sentimeetrites ümardatuna täisarvuks.
#Valem jalalaba pikkuse arvutamiseks on: pikkus = 2/3 * (kinganumber - 2).
#Faili nende ridade juures, kus arvuks teisendamine miskipärast ebaõnnestub,
#tuleb ekraanile kuvada „Vigane sisend” ning jätkata faili järgmise reaga.