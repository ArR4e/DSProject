

def kasutajanimi():
    global kasutajanimi
    kasutajanimi = input("Sisestage soovitud kasutajanimi: ")
    return kasutajanimi

def parooli_sisestamine():
    global parool1
    parool1 = input("Sisestage parool: ")
    global parool2
    parool2 = input("Sisestage parool uuesti: ")
    kontroll_kattuvus(parool1,parool2)
    return parool1, parool2
    

def kirjuta_faili():
    fail = open("users.txt", "w")
    fail.write(str(kasutajanimi) + "." + str(parool2[::-1]))
    fail.close()
    print("ok")

def parool_tagurpidi(parool2):
    return parool2[::-1]

def kontroll_tähed_numbrid(parool2):
    if parool2.upper().isupper() or parool2.isdigit(): #kuidas kontrollida kas paroolis on lisaks tähtedele ka numbrid
        parool_tagurpidi(parool2)
    else:
        print("Parool peab sisaldama nii tähti kui numbreid.")
        parooli_sisestamine()
                        
def kontroll_pikkus(parool2):
    if len(parool2) >= 8:
        kontroll_tähed_numbrid(parool2)
    else:
        print("Parool on liiga lühike (peab olema vähemalt 8 tähemärki)")
        parooli_sisestamine()
def kontroll_kattuvus(parool1, parool2):
    if parool1 != parool2:
        print("Paroolid ei klappinud, proovi uuesti")
        parooli_sisestamine()
    else:
        kontroll_pikkus(parool2)
              
kasutajanimi()
parooli_sisestamine()
kirjuta_faili()
