kasutajanimi = str(input("sisesta kasutajanimi: "))
i = 0
while i < 1:
    parool = str(input("sisesta parool: "))
    parool_uuesti = str(input("sisesta parool uuesti: "))
    if parool == parool_uuesti:
        if len(parool) >= 8:
            if any(i.isdigit() for i in parool) == True:
                parool = parool[::-1]
                i += 1
            else:
                print("paroolis peab olema vähemalt 1 number, proovi uuesti")
        else:
           print("parool liiga lühike, proovi uuesti") 
    else:
        
        print("paroolid ei olnud samad, proovi uuesti")
fail = open("users.txt","w")
fail.write(kasutajanimi + ":" + parool)
fail.close()
print("su kasutajanimi ja parool on lisatud andmebaasi, parool on nüüd teistpidi")
        