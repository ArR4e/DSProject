kasutaja_nimi = input(str("Palun sisesta teie kaustajanimi ja vajuta ENTER: "))
parool = input(str("Palun sisesta oma parooli ja vajuta ENTER: "))
parool1 = input(str("Palun sisesta oma parooli uuesti ja vajuta ENTER: "))
if parool == parool1:
    if len(parool) >= 8:
        if parool.isalnum():
            tag_parool = parool[::-1]
            file = open("users.txt", "w")
            file.write(kasutaja_nimi + ":" + tag_parool)
            file.close()
        if not all(char.isalnum() for char in parool):
            tag_parool = parool[::-1]
            file = open("users.txt", "w")
            file.write(kasutaja_nimi + ":" + tag_parool)
            file.close()
        else:
            print("Palun sisesta oma parooli uuesti! Paroolis on vaja olla nii tähti kui numbreid.")
    else:
        print("Palun sisesta oma parooli uuesti! Parool on vaja olla vähemalt 8 tähemärki pikk")
else:
    print("Palun sisesta oma paroole uuesti! Need on erinevad!")
        
        