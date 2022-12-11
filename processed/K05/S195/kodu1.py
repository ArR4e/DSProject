def numbcheck(parool):
    return any(numb.isdigit()for numb in parool)

def tahtcheck(parool):
    return any(taht.isalpha()for taht in parool)

def tagurpidi(parool):
    parool = parool[::-1]
    return parool


while True:
    kasutajanimi = str(input("Palun sisestage oma kasutajanimi: "))
    parool_yks = str(input("Palun sisestage oma parool:"))
    parool_kaks = str(input("Palun sisestage oma parool teist korda:"))
    if parool_yks == parool_kaks:
        if len(parool_yks) > 7:
            if numbcheck(parool_yks) and tahtcheck(parool_yks):
                break
            else:
                print("Parool peab sisaldama nii tähti ja numbreid.")
        else:
            print("Parool on lühem kui 8 tähemärki.")
    else:
        print("Paroolid ei kattu.")

tagurpidi_parool = tagurpidi(parool_yks)

f = open('users.txt','a')
f.write(kasutajanimi)
f.write(":")
f.write(tagurpidi_parool)
f.close()