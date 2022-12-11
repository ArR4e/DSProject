fnimi = input("Sisesta failinimi: ")
f = open(fnimi,"r",encoding="utf-8")
read = f.readlines()
aegjaraha = []
def sorteeriread(read):
    lõpp = True
    for i in range(len(read)-1):
        if ajaks(read[i].split()[0], read[i+1].split()[0]):
            read[i],read[i+1] = read[i+1],read[i]
            return sorteeriread(read)
            lõpp = False
    if lõpp == True:
        return
def ajaks(aeg1,aeg2):
    esimeneaeg = int(aeg1[:2])*60 + int(aeg1[3:])
    teineaeg = int(aeg2[:2])*60 + int(aeg2[3:])
    if esimeneaeg > teineaeg:
        return True
    elif esimeneaeg == teineaeg:
        return None
    else:
        return False
sorteeriread(read)
prindi = True
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
for võrreldavrida in read:
    
    rida = võrreldavrida.strip("\n").split(" ")
    for uusrida in read:
        uusrida = uusrida.strip("\n").split(" ")
        if ajaks(uusrida[0],rida[0]) and ajaks(rida[1],uusrida[1]) and int(uusrida[2]) < int(rida[2]):
            prindi = False
    if prindi:
        print(võrreldavrida.strip("\n"))
    prindi = True

