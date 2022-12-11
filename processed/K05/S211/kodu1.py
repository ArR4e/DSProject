import string
import re

tähed = string.ascii_letters


kasutaja = input("Sisesta kasutajanimi: ")

while True:
    parool1 = str(input("Sisesta parool: "))
    parool2 = str(input("Sisesta parool uuesti: "))
    parooli_pikkus = len(parool1)
    
    
    if parool1!=parool2:
        print("Paroolid ei kattu! Proovi uuesti.")
        continue
    elif parooli_pikkus < 8:
        print("Parool pole vähemalt 8 tähemärki pikk! Proovi uuesti.")
        continue
    
    elif not (any(chr.isnumeric() for chr in parool1) and any(chr.isascii() for chr in parool1)): 
        print("Pole kasutatud nii tähti kui ka numbreid korraga! Proovi uuesti.")
        continue
    
    else:
        break

tagurpidi = parool1 [::-1]

fail = open("users.txt", "w")

fail.write(kasutaja + ":" + tagurpidi)

fail.close()
        