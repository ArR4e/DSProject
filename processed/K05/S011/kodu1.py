nimi = str(input("Sisesta kasutajanimi: "))
while True:
    parool_1 = (input("Sisesta parool: "))
    parool_2 = (input("Sisesta parool teist korda: "))
    if parool_1 != parool_2 :
        raise Exception ("Paroolid peavad ühtima.")
    elif (len(str(parool_1))) < 8:
        raise Exception ("Parool peab olema vähemalt 8 tähemärki pikk.")
    elif parool_1.isalpha() or parool_1.isdigit():
        raise Exception ("Paroolis peavad olema nii numbrid kui tähed")
    parool_pööratud = (parool_2[::-1])
    break
f= open("users.txt", "w")
f.write(nimi + ":" + parool_pööratud "\n")
f.close()         