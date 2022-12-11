kasutajanimi = input("Sisesta kasutajanimi: ")

def sisalduvad_numbrid(parool):
    for täht in parool:
        if täht.isdigit():
            return True
    return False

while True:
    parool1 = input("Sisesta parool: ")
    parool2 = input("Korda parooli: ")
    if parool1 != parool2:
        print("Paroolid ei kattu.")
        continue
    parooli_pikkus = len(parool1)
    if parooli_pikkus < 8:
        print("Parool on liiga lühike")
        continue
    if sisalduvad_numbrid(parool1) == False:
        print("Paroolis pole numbreid")
        continue
    väike_parool = parool1.lower()
    if väike_parool.islower() == False:
        print("Paroolis puuduvad tähemärgid")
        continue
    else:
        break
    
parool = parool1[::-1]

with open('users.txt', 'w') as f:
    f.write(kasutajanimi + ":" + parool)
    f.close()
    
    