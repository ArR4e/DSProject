kasutajanimi = input(str("Sisesta kasutajanimi: "))
def sisaldab_numbrit(tekst):
    for täht in tekst:
        if täht.isdigit():
            return True
    
    return False
    
def sisaldab_tähte(tekst):
    for täht in tekst:
        if täht.isalpha():
            return True
        
    return False

while True:
    parool_esimestkorda = input("Sisesta parool esimest korda: ")
    parool_teistkorda = input("Sisesta parool teist korda: ")


    if parool_esimestkorda != parool_teistkorda:
        print("Paroolid ei kattu")
        
    elif len(parool_teistkorda) < 8:
        print("Paroolis peab olema vähemalt 8 tähemärki")
    elif not sisaldab_numbrit(parool_teistkorda) or not sisaldab_tähte(parool_teistkorda):
        print("Parool peab sisaldama tähti ja numbreid")
    
    else:
        parooli_pikkus = len(parool_teistkorda)
        parool_tagurpidi = ""
        while parooli_pikkus > 0:
            algus = parooli_pikkus-1
           # print(parool_teistkorda[algus])
            parool_tagurpidi = parool_tagurpidi + parool_teistkorda[algus]
            parooli_pikkus -= 1
            
        print(parool_tagurpidi)
    
        f = open("users.txt", "w")
        f.write(kasutajanimi + ":" + parool_teistkorda)
        f.close()
        break
        
        