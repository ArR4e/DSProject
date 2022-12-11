kasutajanimi = input("Sisestage kasutajanimi: ")

õige_parool = False
parool = input("Sisestage parool: ")

parool2 = input("Sisestage parool uuesti: ")

if parool == parool2:
    if len(parool2) > 8:
        for täht in parool2:
                
            if täht.isdigit() == True:
                õige_parool = True
    else:
        print("Tekkis puudus")
else:
    print("Tekkis puudus")
        
fail = open("users.txt","w")

fail.write(kasutajanimi+":"+parool2[::-1])
fail.close()