def kasonnumber(sõna):
    return any(täht.isdigit() for täht in sõna)

def kasontäht(sõna):
    return any(täht.isalpha() for täht in sõna)

nimi = input("Mis on Teie nimi?: ")

while True:
    parool1 = input("Mis on Teie soovitud parool?: ")
    parool2 = input("Kinnitage valitut (siestage parool uuesti): ")
    if parool1 == parool2:
        if len(parool1) > 7:
            if kasonnumber(parool1) == True and kasontäht(parool1) == True:
                parool = parool1[::-1]
                kirje = nimi+":"+parool
                f = open("users.txt", "w")
                f.write(kirje)
                f.close()
                break
            else:
                print("Parool peab sisaldama nii tähti, kui ka numbreid")
                continue             
        else:
            print("Parool peab olema pikem, kui 7 tähemärki")
            continue
    else:
        print("Paroolid ei kattu")
        continue