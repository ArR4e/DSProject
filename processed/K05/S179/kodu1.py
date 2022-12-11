nimi = input("Sisesta kasutajanimi: ")

while True:
    parool = input("Sisesta parool esimest korda: ")
    paroolKontroll = input("Sisesta parool teist korda: ")
    if parool == paroolKontroll:
        if len(parool) >= 8:
            if parool.isalpha() == False and parool.isnumeric() == False:
                parool = parool[::-1]
                break
            else:
                print("Parool ei sisalda nii tähti kui numbreid!")
        else:
            print("Parool ei ole vähemalt 8 tähemärki pikk!")
    else:
        print("Paroolid ei kattu!")

fail = open("users.txt","a+")
fail.write(f"{nimi}:{parool}\n")
fail.close()

