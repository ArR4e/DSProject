"""https://codefather.tech/blog/check-if-python-string-contains-number/"""
def numbersõnes(sõne):
    for a in sõne:
        if a.isdigit():
            return True

nimi = input("Sisesta kasutajanimi: ")

while True:
    parool1 = input("Sisesta parool: ")
    
    parool2 = input("Sisesta parool uuesti: ")
    
    if parool1 == parool2:
        pass
    else:
        print("Paroolid pole samad")
        continue
        
    if parool1 == parool2 and len(parool1) >= 8:
        pass
    else:
        print("Parool on liiga lühike")
        continue
        
    if parool1 == parool2 and len(parool1) >= 8 \
       and numbersõnes(parool1) == True:
        break
    else:
        print("Paroolis peab olema nii numbreid kui ka tähti")
        continue
        
parool = parool1[::-1]

file = open("users.txt","w",encoding="utf8")
file.write(nimi+":"+parool)
file.close()
        
        
        
        
    