nimi = input("Sisestage kasutajanimi: ")

while True:
    parool1 = input("Sisestage parool esimest korda: ")
    parool2 = input("Sisestage parool  teist korda: ")
    
    if parool1 != parool2:
        print("Esimene parool ei kattu teisega")
        continue
    elif len(parool1)<8:
        print("Parool peab olema vähemalt 8 tähemärki pikk")
        continue
    elif  any(n.isnumeric() for n in parool1) == False:
        print("Paroolis ei ole kasutatud nii tähti kui numbreid")
        continue
    elif  any(a.isalpha() for a in parool1) == False:
        print("Paroolis ei ole kasutatud nii tähti kui numbreid")
        continue
    else:
        stringlength=len(parool1)
        slicedString=parool1[stringlength::-1]
        print(slicedString)
        break
    
f = open("users.txt", "w")
f.write("kasutajanimi:" + nimi + "\n")
f.write("parool:" + parool1 + "\n")

f.close()