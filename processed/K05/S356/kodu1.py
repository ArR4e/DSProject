def tagurpidi(a):
    parool2 = ''
    for i in a:
        parool2 = i + parool2
    return parool2

username = input("Sisesta kasutajanimi: ")

while True:
    parool = input("\nSisesta parool: ")
    parool1 = input("Sisesta parool uuesti: ")

    if parool != parool1:
        print("\nSisestatud paroolid ei ühti")
        
    elif len(parool) < 8:
        print("\nParool peab olema vähemalt 8 tähemärki pikk")
        
    elif parool.isalpha() or parool.isdigit() :
        print("\nParoolis peab kasutama nii tähti kui ka numbreid")
        
    else:
        break
    
paroolreverse = tagurpidi(parool)

f = open("users.txt", "w")
f.write(username + ":" + paroolreverse)
f.close()