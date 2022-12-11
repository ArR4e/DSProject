#Kirjuta programm, mis loeb tekstifailist kinganumbrid.txt sisse EU kinganumbrid
#ja kuvab ekraanile vastavad jalalaba pikkused sentimeetrites ümardatuna
#täisarvuks. Valem jalalaba pikkuse arvutamiseks on:
    #pikkus = 2/3 * (kinganumber - 2).
import time
a = 5

kinganumbrid = open("kinganumbrid.txt")

while a > 0:
    kinganumber = kinganumbrid.readline()
    try:
        kinganumber = float(kinganumber)
        pikkus = 2/3 * (kinganumber - 2)
        pikkus = round(pikkus)
        print(pikkus)
    except:
        if len(kinganumber) == 0:
            break
        print("vigane sisend")