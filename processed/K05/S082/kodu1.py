def kontroll(parool1, parool2):
    if parool1 == parool2:
        if len(parool1) >= 8:
            tahti = 0
            numbreid = 0
            for a in parool1:
                if a.isalpha() == True:
                    tahti+=1
                elif a.isdigit() == True:
                    numbreid +=1
            if tahti == 0 or numbreid == 0:
                print("Paroolis peab olema nii tähti kui numbreid")
                return "uuesti"
            else:
                return "töötab"
            
        else:
            print("Parool on liiga lühike")
            return "uuesti"
    else:       
        print("Paroolid ei ole samad")
        return "uuesti"

nimi = str(input("Sisesta kasutajanimi: "))
parool1 = str(input("Sisesta parool: "))
parool2 = str(input("Sisesta parool teist korda: "))

while True:
    if kontroll(parool1, parool2) == "uuesti":
        parool1 = str(input("Sisesta parool: "))
        parool2 = str(input("Sisesta parool teist korda: "))
    else:
        fail = open("users.txt", "w")
        reverse = parool1[::-1]
        fail.write(nimi)
        fail.write(":")
        fail.write(reverse)
        fail.close()
        break