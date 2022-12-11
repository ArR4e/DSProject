


import re

kasutajanimi = input("Palun sisetage oma kasutajanimi: ")

def parooli_kontroll(x):
    if re.search("[0-9]",x) is not None and re.search ("[^0-9]", x) is not None and len (x) >=8:
        return True
    return False



while True:
    parool = input("Palun sisetage oma parool: ")
    parool2 = input("Palun sisetage oma parool veel kord: ")
    if parool == parool2:
        if len(parool) >= 8:
            if parooli_kontroll(parool):
                loorap = parool[::-1]
                break
            
            else:
                print("Palun veenduge, et parool sisaldab nii tähti kui ka numbreid.")
        else:
            print("Palun veenduge, et parool sisaldab vähemalt 8 tähemärki!")
                    
    else:
        print ("Paroolid on erinevad. Proovige uuesti!")
    
                
with open("users.txt", "w") as file:
    file.write(kasutajanimi + ":" + loorap)

