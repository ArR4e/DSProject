kasutajanimi=input("Sisesta siia oma kasutajanimi :")
parool=input("Sisesta siia oma parool: ")
parool2=input("Sisesta siia oma parool teist korda: ")

#kontrollin, kas paroolid ühtivad
if parool != parool2:
    print("Paroolid ei ühti. Proovi uuesti.")
    while parool != parool2:
        parool=input("Sisesta siia oma parool: ")
        parool2=input("Sisesta siia oma parool teist korda: ")

#kontrollin, kas sisaldab vähemalt 8 märki
if len(parool)<8:
    print("Sisestatud parool on liiga lühike. Sisesta vähemalt 8 tähemärki")
    while len(parool)<8:
        parool=input("Sisesta siia oma parool: ")
        parool2=input("Sisesta siia oma parool teist korda: ")

arv=0
sõna=0
#kontrollin, kas sisaldab tähti ja numbreid
while arv+sõna != 2:    
    for koht in parool:
        if koht.isdigit()==True:
            arv=1
        elif koht.isalpha()==True:
            sõna=1
    if arv+sõna<2:        
        print("Parool peab sisaldama tähti ja numbreid")
        parool=input("Sisesta siia oma parool: ")
        parool2=input("Sisesta siia oma parool teist korda: ")

#järgnev pöörab parooli tagurpidi
pparool=""
for i in parool:
    pparool=i+pparool


f=open(r"C:\Users\Karla\Desktop\python kodutöö\5.nädal\users.txt", "w+")
f.write(kasutajanimi + ":" +pparool)
f.close()