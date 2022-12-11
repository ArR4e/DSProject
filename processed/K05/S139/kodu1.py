def leidubNumber(n):
    a = "0123456789"
    for i in n:
        if i in a:
            return True
    return False



kasutajanimi = input("Sisesta kasutajanimi: ")


while True:
    parool1 = input("Sisesta parool 1. korda: ")
    parool2 = input("Sisesta parool 2. korda: ")
    if parool1 != parool2:
        print("Paroolid ei kattu")
        continue
    elif len(parool1) < 8:
        print("Parool peab vähemalt 8 tähemärki pikk olema")
        continue
    elif leidubNumber(parool1) == False:
        print("Parool peab sisaldama vähemalt 1 numbrit")
        continue
    else:
        break
    
pöörd = ""
for el in parool1:
    pöörd = el + pöörd

    
f = open("users.txt", "a")
f.write(str(kasutajanimi)+":"+ str(pöörd))
f.close()

