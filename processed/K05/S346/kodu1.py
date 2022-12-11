kasutajanimi = str(input("Sisesta kasutajanimi: "))
while True:
    parool1 = str(input('Sisesta parool esimest korda: '))
    parool2 = str(input('Sisesta parool teist korda: '))
    if parool1 == parool2:
        len(parool1)
        if len(parool1) >= 8:
            if parool1.isalnum():
                f = open("users.txt","w")
                reversed_parool1 = parool1[::-1]
                f.write(kasutajanimi)
                f.write(":")
                f.write(reversed_parool1)
                f.close()
                break
            if not all(i.isalnum() for i in parool1):
                f = open("users.txt","w")
                reversed_parool1 = parool1[::-1]
                f.write(kasutajanimi)
                f.write(":")
                f.write(reversed_parool1)
                f.close()
                break
            else:
                print("Sõna peab sisaldama nii tähti kui numbreid")
        else:
            print("Sõnas peab olema vähemalt 8 tähemärki pikk")
    else:
        print("Esimene parool ei kattu teise parooliga")