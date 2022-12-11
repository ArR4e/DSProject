def ontähed(parool):
    return any(char.isalpha() for char in parool)
def onnumbrid(parool):
    return any(char.isdigit() for char in parool)
kasutajanimi = input("Sisestage kasutajanimi:")
while True:
    parool = str(input("Sisestage parool esimest korda:"))
    parool2 = str(input("Sisestage parool teist korda:"))
    tähearv = 0 
    if parool == parool2:
        for i in range(len(parool)):
            tähearv += 1
        if tähearv >= 8:
            if ontähed(parool) and onnumbrid(str(parool)):
                a = open("users.txt", "w")
                a.write(kasutajanimi +":" + parool[::-1])
                a.close()
                break
            else:
                print("Parool peab sisaldama numbreid ja tähti")
                continue
        else:
            print("Parool peab olema vähemalt 8 tähemärki.")
            continue
            
    else:
        print("Esimene ja teine parool ei ole samad")
    continue
