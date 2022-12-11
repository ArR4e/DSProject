nimi= input("sisesta kasutajanimi:")
f=open("users.txt","w")

def sisaldabnr(n):
    for i in parool1:
        if i.isdigit():
            return True
    return False

while True:
    parool1=input("sisesta parool:")
    parool2=input("Sisesta parool uuesti:")
    l=len(parool1)
    paroolv=str.lower(parool2)
    

    if parool1==parool2 and len(parool1)>=8 and str.islower(paroolv)==True and sisaldabnr(parool1)==True:
            f.write(nimi+":".strip())
            f.write(parool1[::-1])
            f.close()
            break
    elif parool1!=parool2:
        print("Sinu paroolid ei kattu")
        continue
    elif str.islower(paroolv)!=True or sisaldabnr(parool1)!=True:
        print("Sinu parool peab sisaldama tähti ja numbreid")
        continue
    else:
        print("Sinu parooli pikkus peab olema vähemalt 8 tähemärki")
        continue