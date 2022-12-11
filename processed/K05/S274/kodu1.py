kasutajanimi = input("Sisesta oma kasutajanimi: ")
parool1 = input("Sisesta parool esimest korda: ")
parool2 = input("Sisesta parool teist korda: ")

while True:
    if parool1 != parool2:
        print("Sisestatud paroolid ei kattu, proovi uuesti!")
        parool1 = input("Sisesta parool esimest korda: ")
        parool2 = input("Sisesta parool teist korda: ")
        
    elif len(parool1) < 8 or len(parool2) < 8:
        print("Parool on lühem kui kaheksa tähemärki, proovi uuesti!")
        parool1 = input("Sisesta parool esimest korda: ")
        parool2 = input("Sisesta parool teist korda: ")
        
    elif parool1.isdigit() or parool1.isalpha():
        print("Parool peab koosnema tähtedest ja numbritest!")
        parool1 = input("Sisesta parool esimest korda: ")
        parool2 = input("Sisesta parool teist korda: ")
    
    else:
        break
parool = parool1[::-1] #leid internetist
tulemus = kasutajanimi + ":" + parool
f = open("users.txt", "w")
f.write(tulemus)
f.close()

                    