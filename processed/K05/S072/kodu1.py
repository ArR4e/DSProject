def küsi_parooli():
    parool1 = input("Palun sisestage oma parool: ")
    parool2 = input("Palun sisestage oma parool uuesti: ")
    
    if parool1 != parool2:
        print("Paroolid ei ühti!")
        küsi_parooli()
    elif len(parool1) < 8:
        print("Parool on lühem kui 8 tähemärki!")
        küsi_parooli()
    elif len([x for x in parool1 if x.isdigit()]) == 0 or len([x for x in parool1 if x.isalpha()]) == 0:
        print("Parool peab sisaldama nii tähti kui numbreid!")
        küsi_parooli()
    else:
        parool1 = parool1[::-1]
        with open("users.txt", "w") as f:
            f.write(kasutajanimi + ':' + parool1)
            
kasutajanimi = input("Palun sisestage oma kasutajanimi: ")
küsi_parooli()


