#kodu1 - plokkskeem

#Küsime kasutajalt nime ja parooli
kasutajanimi = input(str("Palun sisestage kasutajanimi: "))
parool1 = input("Palun sisestage parool: ")
parool2 = input("Palun sisestage parool teist korda: ")

#Kontrollime, kas parool1 ja parool2 kattuvad
while parool1 != parool2:
    print("Sisestatud paroolid ei kattu!")
    parool1 = input("Palun sisestage parool: ")
    parool2 = input("Palun sisestage parool teist korda: ")
    #Kontrollime, kas parool on 8 tähemärki pikk
while len(parool1) <= 8:
    print("Parool peab olema vähemalt 8 tähemärki pikk!")
    parool1 = input("Palun sisestage parool: ")
    parool2 = input("Palun sisestage parool teist korda: ")
        #Kontrollime, kas paroolis on tähti ja numbreid
while parool1.isalpha() or parool1.isnumeric():
    print("Parool peab sisaldama numbreid ja tähti!")
    parool1 = input("Palun sisestage parool: ")
    parool2 = input("Palun sisestage parool teist korda: ")
   
krüpteeritud = str(parool1[::-1])
sihtf = open("users.txt", "w")
sihtf.write(kasutajanimi + ":" + krüpteeritud)

sihtf.close()

       