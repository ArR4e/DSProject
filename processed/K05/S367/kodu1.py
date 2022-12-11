kasutajanimi = input("Sisesta kasutajanimi: ")
parool = input("Sisesta parool: ")
parool_2 = input("Sisesta parool teist korda: ")
while True:
    if parool_2 == parool:
        if len(parool) < 8:
            print("Teie paroolis peab olema vähemalt 8 tähemärki.")
        elif parool.isdigit() and parool.isalpha(parool):
            tagurpidi = ''.join(reversed(parool))
            print (tagurpidi)