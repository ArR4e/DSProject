kasutajanimi=input("Sisesta kasutajanimi: ")

tähti=0
numbreid=0
    #return (tähti,numbreid) see käib automaatselt

while True:
    parool1=input("Sisesta parool: ")
    parool2=input("Sisesta parool uuesti: ")
    if len(parool1)<8:
        print("Parool on lühikesevõitu. Vali parool, mis on vähemalt 8 tähemärki pikk.")
        continue
    for i in parool1:
        if i.isalpha():
            tähti+=1
        elif i.isdigit():
            numbreid+=1
    if tähti<1 or numbreid<1:
        print("Paroolis peab olema vähemalt üks täht ja vähemalt 1 number. Proovi uuesti!")
    elif parool1!=parool2:
        print("Paroolid ei kattu. Proovi uuesti!")
    elif parool1==parool2:
        break
    
with open("users.txt", "w") as sihtfail:
    sihtfail.write(kasutajanimi+(parool1[::-1]))

    