#Kusib aastatulu summa kohta
aastatulu=float(input("Sisesta aastatulu: "))
#Maksuvabatulu arvutamise valemi sisestamine
maksuvabatulu=(6000-(6000/10800)*(aastatulu-14400))
#Maksuvabatulu kui aastatulu on kuni 6000 eurot
if aastatulu <= 6000:
    print("Maksuvaba tulu on " + str(aastatulu) + " eurot.")
#Maksuvabatulu kui aastatulu on 6000-14400 eurot
elif aastatulu >= 6000 and aastatulu <=14400:
    print("Maksuvaba tulu on 6000 eurot aastas.")
#Maksuvabatulu kui aastatulu on 14400-25200 eurot, siin rakendatakse 4 rea valemit ja umardatakse loppvastus    
elif aastatulu >= 14400 and aastatulu <= 25200:
    print("Maksuvaba tulu on", round(maksuvabatulu , 2) ,"eurot.")
#maksuvabatulu kui aastatulu on ule 25200 euro    
elif aastatulu >= 25200:
    print("Maksuvaba tulu on 0 eurot.")