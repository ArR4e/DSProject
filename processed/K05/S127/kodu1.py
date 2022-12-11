kasutajanimi= input("Sisestage kasutajanimi: ")
parool1= input("Sisestage parool: ")
parool2= input("Korrake parooli: ")
while parool1!=parool2:
    print("Sisestatud paroolid ei ole samasugused. Proovige veel! ")
    parool1= input("Sisestage parool: ")
    parool2= input("Korrake parooli: ")
while len(parool1)<8:
    print("Parool on liiga lühike. Proovige veel! ")
    parool1= input("Sisestage parool: ")
    parool2= input("Korrake parooli: ")
while parool1.isalpha()== True or parool1.isdigit()== True:
    print("Parool peab sisaldama nii tähti kui numbreid. Proovige veel! ")
    parool1= input("Sisestage parool: ")
    parool2= input("Korrake parooli: ")
parool=parool1[::-1]
f = open("users.txt", "w")
f.write(kasutajanimi + ":" + parool)
f.close()
    