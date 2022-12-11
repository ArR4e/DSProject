kasutajanimi=input("Sisestage oma kasutajanimi: ")
while True:
    parool1=input("Sisestage oma parool: ")
    parool2=input("Sisestage oma parool teist korda: ")
    if parool1!=parool2:
        print("Viga! Sisestatud paroolid ei kattu omavahel!")
        continue
    paroolipikkus=len(parool1)
    if paroolipikkus<8:
        print("Viga! Sisesatud parool on alla 8 tähemärgi pikk!")
        print("Sisestage parool, mis on vähemalt 8 tähemärki pikk.")
        continue
    if parool1.isnumeric() or parool1.isalpha():
        print("Viga! Parool peab sisaldama nii tähti kui ka numbreid!.")
        continue
    break
i=-1
krüpteering=str()
while i>=-paroolipikkus:
    täht=parool1[i]
    krüpteering+=täht
    i-=1
f=open("users.txt", mode="w")
f.write(kasutajanimi+':'+krüpteering)
f.close()