kasutajanimi = str(input("Sisestage kasutajanimi: "))


def parooli_validaator():
    while True:
        esimene = str(input("Sisestage parool: "))
        teine = str(input("Sisestage parool teist korda: "))
        if esimene != teine:
            print("Teine parool on esimesest erinev!")
        elif len(esimene) < 8:
            print("Teie paroolis peab olema vähemalt 8 tähemärki!")
        elif any(char.isdigit() for char in esimene) == False:
            print("Teie paroolis peab olema vähemalt 1 number!")
        elif any(char.isalpha() for char in esimene) == False:
            print("Teie paroolis peab olema vähemalt 1 täht!")
        else:
            break
    return esimene



f = open("users.txt", "w")
f.write(kasutajanimi + ':' + str(parooli_validaator())[::-1])
f.close()