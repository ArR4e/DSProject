def kasutajaparool ():
    while True:
        num = 0
        täht = 0
        parool = input("Palun sisestage parool:")
        kontroll = input("Palun sisestage parool uuesti:")
        
        if parool != kontroll:
            print("Sisestatud paroolid ei kattu")
        elif len(parool) < 8:
            print ("Sisestatud parool on lühem kui 8 tähemärki")
        else:
            for i in parool:
                if i.isdigit():
                    num = 1
                elif i.isalpha():
                    täht = 1
            if täht+num == 2:
                return parool
            else:
                print("Paroolis pole kasutatud nii numbreid kui ka tähti")
def kirjuta(kasutajanimi,parool):
    parool = parool[::-1]
    with open("users.txt", "w") as f:
        f.write(kasutajanimi+":"+parool+ "\n")

kirjuta(input("Sisestage Kasutajanimi:"), kasutajaparool ())