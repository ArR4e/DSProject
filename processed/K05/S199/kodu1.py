
def kasutaja():
    kasutajanimi = str(input("Sisestage oma kasutajanimi: "))
    
    while True:
        parool1 = str(input("Sisestage oma parool: "))
        parool2 = str(input("Sisestage oma parool veel üks kord: "))
        parooli_pikkus = len(parool1)

        if parool1 != parool2:
            print("Kirjutatud paroolid ei kattu!")
            continue
        
        elif len(parool1) < 8:
            print("Sisestatud parool on liiga lühike!")
            continue
        
        elif parool1.isalpha() == True or parool1.isnumeric() == True:
            print("Parool peab sisaldama nii numbreid kui ka tähti!")
            continue
        else:
            tagurpidi_parool =parool1[parooli_pikkus::-1]
            kirjutis = (kasutajanimi + ":" + tagurpidi_parool)
            f = open("users.txt", "w")
            f.write(kirjutis + "\n")
            f.close()
            break
            
kasutaja()
