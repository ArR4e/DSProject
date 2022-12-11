def sisestus(x):
    if x == 1:
        return input("palun sisesta parool: ")
    elif x==2:
        return input("palun sisesta uuesti parool: ")
def pööra(parool,suurj):
    x = suurj - 1
    originaal = [x]
    uus = [x]
    m1 = 0
    for märk in parool:
        originaal.insert(m1, märk)
        m1 = m1 + 1
    m1 = 0
    while m1 != suurj:
        uus.insert(m1, originaal[x])
        x = x-1
        m1=m1+1
    return uus

while True:
    kasutajanimi=input("Palun sisesta kasutajanimi: ")
    while True:
        parool1 = sisestus(1)
        parool2 = sisestus(2)
        pikkus = len(parool1)
        if parool1 == parool2:
            if pikkus>=8:
                if any(chr.isdigit() for chr in parool1) == True and any(chr.isalpha() for chr in parool1) == True:
                    break
                else:
                    print("Sisestatud parool ei sisalda nii numbreid kui tähti, palun proovi uuesti")
            else:
                print("Sisestatud parooli pikkus on alla 8 tähemärgi, palun proovi uuesti")
        else:
            print("Sisestatud paroolid ei kattu, palun proovi uuesti")
        
    encryp = pööra(parool1,pikkus)
    f = open("users.txt", "a")
    f.write(kasutajanimi)
    f.write(":")
    muut1 = 0
    while muut1 != pikkus:
        f.write(encryp[muut1])
        muut1 = muut1 + 1
    f.close()
    break