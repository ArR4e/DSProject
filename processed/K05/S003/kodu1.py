kasutajanimi = str(input("Palun sisesta kasutajanimi "))
def onnumbreid(sõne):
    for i in sõne:
        if i.isnumeric():
            return True
    return False

def ontähti(sõne):
    for i in sõne:
        if i.isnumeric():
            return True
    return False


while True :
    parool1 = str(input("Palun sisesta parool "))
    parool2 = str(input("Palun sisesta parool teist korda "))
    if parool1 != parool2:
        print("paroolid ei kattu!")
        continue
    if len(parool1) < 8:
        print("parool on lühem kui 8 tähemärki")
        continue
    if onnumbreid(parool1) == False or ontähti(parool1) == False:
        print("sõnes poe kasutatud nii tähti kui ka numbreid")
        continue
    break
parool = parool1[::-1]
f = open("users.txt","w")
f.write(kasutajanimi + ":" + parool)
f.close()
