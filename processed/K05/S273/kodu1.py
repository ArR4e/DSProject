
def kasnumber(parool):
    for karakter in parool:
        if karakter.isdigit():
            return True
    return False

def kastäht(parool):
    for karakter in parool:
        if karakter.isalpha():
            return True
    return False

def pööraParool(parool):
    parooliPikkus = len(parool)
    pööratudParool = parool[parooliPikkus::-1]
    return(pööratudParool)



kasutajanimi = input("Sisestage kasutajanimi: ")

while True:
    parool1 = input("Sisestage parool: ")
    parool2 = input("Sisestage parool uuesti: ")
    
    if parool1 != parool2:
        print("Sisestasite erinevad paroolid!")
        continue
    elif len(parool1) < 8:
        print("Parool on liiga lühike!")
        continue
    elif kasnumber(parool1) == True and kastäht(parool1) == True:
        fail = open("users.txt", "w")
        fail.write(kasutajanimi + ":" + pööraParool(parool1))
        fail.close()
        print("Tehtud")
        break
    else:
        print("Paroolis peab olema nii arv, kui ka täht")
        continue
        
        
    
        