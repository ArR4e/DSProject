kasutajanimi = input("Sisestage kasutajanimi: ")
def on_numbreid(parool):
    for number in parool:
        try:
            int(number)
            return True
        except:
            continue
    else:
        return False
while True:
    parool1 = input("Sisestage parool: ")
    parool2 = input("Sisestage parool uuesti: ")
    if parool1 != parool2:
        print("Teie paroolides tuvastati erinevus, palun proovige uuesti.")
        continue
    elif len(parool1) < 8:
        print("Teie parool pole vähemalt 8 tähemärki pikk, palun proovige uuesti.")
        continue
    elif on_numbreid(parool1) == False:
        print("Teie parool peab sisaldama vähemalt ühte numbrit, palun proovige uuesti.")
        continue
    else:
        break
users = open("users.txt","w")
users.write(kasutajanimi+":"+str(parool1[len(parool1)::-1]))
users.close()
        