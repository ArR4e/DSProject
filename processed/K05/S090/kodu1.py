nimi = input("Sisestage kasutajanimi: ")
parool = input("Sisestage parool: ")
parool2 = input("Sisestage parool uuesti: ")
if parool == parool2:
    if len(parool) >= 8:
        if parool.isalpha() == False and parool.isnumeric() == False:
            tagurpidi = parool[::-1]
            fail = open("users.txt", "w")
            fail.write(nimi+":"+tagurpidi)
            fail.close()
        else:
            print("Proovige uuesti")
    else:
        print("Proovige uuesti")
else:
    print("Proovige uuesti")
