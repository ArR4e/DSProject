liin = int(input("Liini pikkus "))
kaugus = int(input("Kõrvutiasetsevate postide maksimaalkaugus: "))
summa= liin//kaugus+1
if liin % kaugus != 0:
    summa +=1
print("Vaja on " + str(summa) + " posti")