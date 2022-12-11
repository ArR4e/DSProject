kasutajanimi = str(input("Sisestage oma kasutajanimi: "))
parool1 = str(input("Sisestage soovitud parool: "))
parool2 = str(input("Korrake oma soovitud parooli: "))

if parool1 != parool2:
    print("Paroolid ei kattu!")
    parool1 = str(input("Sisestage soovitud parool: "))
    parool2 = str(input("Korrake oma soovitud parooli: "))
    
elif len(parool1)<8:
    print("Soovitud parooli pikkus on liiga lühike.")
    parool1 = str(input("Sisestage soovitud parool: "))
    parool2 = str(input("Korrake oma soovitud parooli: "))
    
elif parool1.isalpha() == True and parool1.isnumeric() == True:
    loorap = parool1[:: -1]
    f = open("user.txt", "w")
    f.write(kasutajanimi+ ":" + loorap)
    f.close()
else:
    print("Parool peaks sisaldama tähti ning numbreid.")
    parool1 = str(input("Sisestage soovitud parool: "))
    parool2 = str(input("Korrake oma soovitud parooli: "))