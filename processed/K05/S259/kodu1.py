def konto():
    while True:
        num = 0
        täht = 0
        parool = input("Sisesta parool: ")
        kontroll = input("Sisesta parool teist korda: ")
        
        if parool != kontroll:
            print("Paroolid ei kattu.")
        elif len(parool) < 8:
            print("Parool peab olema vähemalt 8 tähemärki pikk.")
        else:
            for i in parool:
                if i.isdigit(): #kontrollib numbri olemasolu
                    num = 1
                elif i.isalpha(): #kontrollib tähe olemasolu
                    täht = 1
            if num + täht == 2: #kontrollib kõiki nõudeid
                return parool
            else:
                print("Parool peab sisaldama nii tähti kui numbreid.")

def kontotoiming(kasutajanimi, parool):
    parool = parool [::-1] #kirjutab tagurpidi
    with open("users.txt", 'w') as f: #kirjutab faili 2 rida
        f.write(kasutajanimi+":"+parool+'\n')

kontotoiming(input("Sisesta kasutajanimi: "), konto()) #kutsub funktsiooni välja