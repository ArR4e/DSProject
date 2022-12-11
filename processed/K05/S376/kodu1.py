kasutajanimi = str(input("Sisesta kasutajanimi: "))

kattuvus = ""
pikkus = ""
sisaldab_nr = ""
sisaldab_tähti = ""
sisu = ""

while kattuvus != True or pikkus != True or sisu != True:
    parool1 = str(input("Sisesta parool: "))
    parool2 = str(input("Sisesta parool uuesti: "))

    if parool1 == parool2:
        kattuvus = True
    else:
        print("Paroolid ei kattu")
        kattuvus = False
        continue
        
    if len(parool1) >= 8:
        pikkus = True
    else:
        print("Parool ei ole 8 tähemärki pikk")
        pikkus = False
        continue

    for sümbol in parool1:
        
        if sümbol.isalpha():
            sisaldab_tähti = True
        
        if sümbol.isdigit():
            sisaldab_nr = True
        
    if sisaldab_nr == True and sisaldab_tähti == True:
        sisu = True
    else:
        print("Paroolis pole kasutatud kas numbreid või tähti")
        sisu = False
        continue

tagurpidi_parool = parool1 [::-1]

f = open("users.txt", "w")
f.write(kasutajanimi + ":" + tagurpidi_parool)
f.close()