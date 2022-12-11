kasutajanimi = input("Sisestage kasutajanimi: ")
sihtfail = "users.txt"
sf = open(sihtfail, "w")

while True:
    parool = input("Sisestage parool: ")
    p_kontroll = input("Sisestage parool uuesti: ")
    if parool == p_kontroll:
        pikkus = len(parool) 
        täht = False # hilisemaks kasutamiseks, et leida kas parool sisaldab tähti
        number = False # hilisemaks kasutamiseks, et leida kas parool sisaldab tähti
        uus = "" # hilisemaks kasutamiseks, et parooli tagurpidi pöörata
        if pikkus >= 8:
            for i in parool: # kontrollimiseks kas paroolis on tähti ja numbreid
                if i.isdigit():
                    number = True
                elif i.isalpha():
                    täht = True
            if number == True and täht == True:
                while pikkus > 0:
                    uus += parool[pikkus - 1] #parooli tagurpidi kirjutamiseks
                    pikkus -= 1
                sf.write(kasutajanimi + ":" + uus)
                sf.close()
                break
            else:
                print("Parool peab sisaldama nii numbreid kui ka tähti!")
            
        else:
            print("Parool peab sisaldama vähemalt 8 tähemärki!")
    else:
        print("Paroolid ei kattu!")