#plokkskeem

kasutaja=input("Sisesta kasutajanimi: ")

while True:
    parool1=input("Sisesta parool: ")
    parool2=input("Sisesta parool uuesti: ")
    if parool1!=parool2:
        print("Paroolid ei kattu!")
        continue
    if len(parool1)<8:
        print("Parool peab olema vähemalt 8 tähemärki pikk!")
        continue
    arve=0
    tähti=0
    for letter in parool1:
        a=letter
        try:
            b=int(a)
            arve+=1
        except:
            tähti+=1
    if arve==0 or tähti==0:
        print("Parool peab sisaldama nii tähti kui ka numbreid!")
        continue
    #kui on siiani ära jõudnud lihtsalt siis on kõik ok
    break

#pööra tagurpidi
uus_parool=""
for letter in parool1:
    a=letter
    uus_parool=a+uus_parool
    
f=open("users.txt", "w")
f.write(kasutaja+":"+uus_parool)
f.close()
            