kasutajanimi = str(input("Mis on sinu kasutajanimi? "))
def küsi():
    global parool1
    global parool2
    parool1 = str(input("Mis on sinu parool? "))
    parool2 = str(input("Sisesta parool uuesti. "))
    return [parool1, parool2]
def kattuvad():
    if parool1 != parool2:
        print("Paroolid ei kattu")
        return False
    else:
        return True
def piisavaltpikk():
    if len(parool1) < 8:
        print("Parool pole piisavalt pikk")
        return False
    else:
        return True
def sisu():
    if parool1.isalpha() == True or parool1.isnumeric() == True:
        print("Paroolis ei ole kasutatud nii tähti kui ka numbreid")
        return False
    else:
        return True
while True:
    küsi()
    if kattuvad() == False:
        continue
    if piisavaltpikk() == False:
        continue
    if sisu() == False:
        continue
    else:
        print("Parool sobib, kirjutan faili.") 
        break
sõnapikkus = len(parool1)
teistpidi = parool1[sõnapikkus::-1]
fail = open("users.txt", "w")
fail.write(kasutajanimi)
fail.write(":")
fail.write(teistpidi)
fail.close()