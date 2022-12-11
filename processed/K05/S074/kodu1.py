#Impordin vajaliku mooduli
import re
#Kasutajanime sisestamine
kasutajanimi = input("Sisesta oma kasutajanimi: ")
#Defineerin funktsiooni, mis kontrollib, kas parool sobib ja kas mõlemad paroolid kattuvad omavahel
def parool():
    while True:
        parool1 = input("Sisesta siia oma parool: ")
        parool2 = input("Korda oma parooli: ")
        if parool1 != parool2:
            print("Paroolid ei sobi omavahel!")
        elif len(parool1) < 8:
            print("Sisestatud parool on liiga lühike!")
        elif re.search ("[0-9]", parool1) is None:
            print("Parool peab sisaldama vähemalt ühte numbrit ja tähte")
        elif re.search("[a-z-A-Z]", parool1) is None:
            print("Parool peab sisaldama vähemalt ühte tähte ja numbrit!")
#Kirjutan kasutaja nime ja parooli (tagurpidi) faili users.txt
        else:
            f = open("users.txt" , "w")
            f.write(  kasutajanimi + ":"  + parool1[::-1] )
            f.close()
            print("Sinu paroolid sobisid omavahel, kasutajanime ja prooli leiad failist users.txt")
            break
parool()
