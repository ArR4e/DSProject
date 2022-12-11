kasutajanimi = input("Sisestage oma kasutajanimi: ")
tähed = "qwertyuiopüõasdfghjklöäzxcvbnmQWERTYUIOPÜÕASDFGHJKLÖÄZXCVBNM"
numbrid = "1234567890"
is_täht = 0
is_num = 0
while True:
    parool = input("Sisestage oma parool: ")
    parool1 = input("Sisestage oma parool uuesti: ")
    
    if parool != parool1:
        print("Parooli sisestused ei klapi \n")
        continue
    
    if len(parool) < 8:
        print("Parool pole piisavalt pikk \n")
        continue
    
    for i in parool:
        if i in tähed:
            is_täht = 1
            if is_num == 1:
                break
        elif i in numbrid:
            is_num = 1
            if is_täht == 1:
                break
    if is_täht + is_num != 2:
        print("Parool peab sisaldama nii tähti kui numbreid \n")
        continue
    break

pööratud = parool[len(parool) : : -1]
with open("users.txt", "w" ) as fail:
    fail.write(kasutajanimi + ":" + pööratud)